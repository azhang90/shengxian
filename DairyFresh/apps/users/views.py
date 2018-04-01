from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import User,AreaInfo,Address
from django.views.generic import View
from django.core.mail import send_mail
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired
import re
from celery_tasks.tasks import send_user_active
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from utils.views import LoginRequiredViewMixin
from django_redis import get_redis_connection
from goods.models import GoodsSKU
import json


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        dict = request.POST
        uname = dict.get('user_name')
        pwd = dict.get('pwd')
        cpwd = dict.get('cpwd')
        email = dict.get('email')
        allow = dict.get('allow')
        context = {
            'uname':uname,
            'pwd':pwd,
            'cpwd':cpwd,
            'email':email,
            'allow':allow,
            'err_msg':'',
        }
        if allow is None:
            context['err_msg'] = '请接收协议'
            return render(request,'register.html',context)

        if not all([uname,pwd,cpwd,email]):
            context['err_msg'] = '数据不能为空'
            return render(request,'register.html',context)

        if pwd != cpwd:
            context['err_msg'] = '两次密码输入不一致'
            return render(request,'register.html',context)

        if User.objects.filter(username=uname).count()>0:
            context['err_msg'] = '用户名已经存在'
            return render(request,'register.html',context)

        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            context['err_msg'] = '邮箱格式不正确'
            return render(request,'register.html',context)


        user = User.objects.create_user(uname,email,pwd)
        user.is_active = False
        user.save()

        #
        # serializer = Serializer(settings.SECRET_KEY, 60 * 60)
        # value = serializer.dumps({'id': user.id}).decode()
        # #
        # msg = '<a href="http://127.0.0.1:8000/user/active/%s">点击激活</a>' % value
        # send_mail('天天生鲜-账户激活', '', settings.EMAIL_FROM, [email], html_message=msg)

        send_user_active.delay(user.id,user.email)

        return HttpResponse('注册成功')

def active(request,value):
    try:
        serializer = Serializer(settings.SECRET_KEY)
        dict = serializer.loads(value)
    except SignatureExpired as e:
        return HttpResponse('邮件已过期')

    uid = dict.get('id')
    user = User.objects.get(pk=uid)
    user.is_active = True
    user.save()

    return redirect('/user/login')

class LoginView(View):
    def get(self,request):
        uname = request.COOKIES.get('uname','')
        context = {
            'title':'登录',
            'uname':uname
        }
        return render(request,'login.html',context)
    def post(self,request):
        dict = request.POST
        uname = dict.get('username')
        pwd = dict.get('pwd')
        remember = dict.get('remember')
        context = {
            'uname':uname,
            'pwd':pwd,
            'err_msg': '',
            'title':'登录处理',

        }

        if not all([uname,pwd]):
            context['err_msg'] = '请填写完整信息'
            return render(request,'login.html',context)

        # user = User.objects.create_user(uname, pwd)
        user = authenticate(username=uname,password=pwd)

        if user is None:
            context['err_msg'] = '用户名或密码错误'
            return render(request,'login.html',context)

        if not user.is_active:
            context['err_msg'] = '邮箱未激活，请先激活邮箱'
            return render(request,'login.html',context)

        login(request,user)

        # return redirect('/user/info')
        response = redirect('/user/info')

        next_url = request.GET.get('next', '/user/info')
        response = redirect(next_url)


        # 记住用户名g`g
        if remember is None:
            response.delete_cookie('uname')
        else:
            response.set_cookie('uname', uname, expires=60 * 60 * 24 * 7)


        cart_str = request.COOKIES.get('cart')
        if cart_str:
            # 将购物车中的信息转存到ｒｅｄｉｓ中
            key = 'cart%d' % request.user.id
            redis_client = get_redis_connection()
            cart_dict = json.loads(cart_str)
            for k,v in cart_dict.items():
                # 判断ｒｅｄｉｓ中是否存在这个商品
                if redis_client.hexists(key,k):
                    count1 = int(redis_client.hget(key,k))
                    count2 = v
                    count0 = count1 + count2
                    redis_client.hset(key,k,count0)
                else:
                    redis_client.hset(key,k,v)
            response.delete_cookie('cart')

        # 如果登录成功则转到用户中心页面
        return response

def logout_user(request):
    logout(request)
    return redirect('/user/login')

@login_required
def info(request):
    # 如果用户未登录，则转到登录页面
    # if not request.user.is_authenticated():
    #     return redirect('/user/login?next='+request.path)

    # 查询当前用户的默认收货地址,如果没有数据则返回[]
    address = request.user.address_set.filter(isDefault=True)
    if address:
        address = address[0]
    else:
        address = None

    # 获取redis服务器的连接,根据settings.py中的caches的default获取
    redis_client = get_redis_connection()
    # 因为redis中会存储所有用户的浏览记录，所以在键上需要区分用户
    gid_list = redis_client.lrange('history%d' % request.user.id, 0, -1)
    # 根据商品编号查询商品对象
    goods_list = []
    for gid in gid_list:
        goods_list.append(GoodsSKU.objects.get(pk=gid))

    context = {
        'title': '个人信息',
        'address': address,
        'goods_list': goods_list
    }
    return render(request, 'user_center_info.html', context)


@login_required
def order(request):
    context = {}
    return render(request,'user_center_order.html',context)

class SiteView(LoginRequiredViewMixin,View):
    def get(self,request):
        addr_list = Address.objects.filter(user=request.user)
        context = {
            'addr_list': addr_list,
            'title':'收货地址'
        }
        return render(request,'user_center_site.html',context)

    def post(self,request):
        # 接收数据
        dict = request.POST
        receiver = dict.get('receiver')
        provice = dict.get('provice')  # 选中的option的value值
        city = dict.get('city')
        district = dict.get('district')
        addr = dict.get('addr')
        code = dict.get('code')
        phone = dict.get('phone')
        default = dict.get('default')

        # 验证有效性
        # if not all([receiver, provice, city, district, addr, code, phone]):
        #     return render(request, 'user_center_site.html', {'err_msg': '信息填写不完整'})

        # 保存数据
        address = Address()
        address.receiver = receiver
        address.province_id = provice
        address.city_id = city
        address.district_id = district
        address.addr = addr
        address.code = code
        address.phone_number = phone
        if default:
            address.isDefault = True
        address.user = request.user
        address.save()

        # 返回结果
        return redirect('/user/site')

def area(request):
    pid = request.GET.get('pid')

    if pid is None:
        # 查询省信息[area,]
        slist = AreaInfo.objects.filter(aParent__isnull=True)
    else:
        # 查询指定pid的子级地区
        # 如果pid是省的编号，则查出来市的信息
        # 如果pid是市的编号，则查出来区县的信息
        slist = AreaInfo.objects.filter(aParent_id=pid)

    slist2 = []
    for s in slist:
        slist2.append({'id':s.id,'title':s.title})

    return JsonResponse({'list':slist2})




        # def register(request):
#     # return HttpResponse('ok')
#     return render(request,'register.html')