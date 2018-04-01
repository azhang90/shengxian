from django.shortcuts import render
from django.http import JsonResponse,Http404
from goods.models import GoodsSKU
# from django_redis import get_redis_connection
import json
from django_redis import get_redis_connection

# Create your views here.
def add(request):
    if request.method != 'POST':
        return Http404()

    # 接收商品编号数量
    dict = request.POST
    sku_id = dict.get('sku_id')
    count = int(dict.get('count',0))

    # 验证数据有效性
    # 判断编号是否合法
    if GoodsSKU.objects.filter(id=sku_id).count() <= 0:
        return JsonResponse({'status':2})

    #　判断数量是否合法
    if count <= 0:
        return JsonResponse({'status':3})
    if count >= 5:
        count = 5
    response = JsonResponse({'status':1})
    # 区分用户是否登陆
    if request.user.is_authenticated():
        # 如果登陆则购物车信息保存到ｒｅｄｉｓ中
        redis_client = get_redis_connection()
        key = 'cart%d'%request.user.id
        if redis_client.hexists(key,sku_id):
            count1 = int(redis_client.hget(key,sku_id))
            count2 = count
            count0 = count1 + count2
            redis_client.hset(key,sku_id,count0)
        else:
            redis_client.hset(key,sku_id,count)

        total_count = 0
        for v in redis_client.hvals(key):
            total_count += int(v)
        response = JsonResponse({'status':1,'total_count':total_count})


    else:
        # 如果没登陆，信息保存到ｃｏｏｋｉｅｓ中

        # 先构造一个字典，用于存放购物车的数据
        cart_dict = {}

        # 读取ｃｏｏｋｉｅｓ中的购物车信息，
        cart_str = request.COOKIES.get('cart')

        # 判断购物车信息是佛已经存在，如果存在将购物车信息转换为字典
        if cart_str:
            cart_dict = json.loads(cart_str)

        # 判断购物车中是否有ｓｋｕ_id商品，如果商品已经存在则数量相加，并加入购物车
        if sku_id in cart_dict:
            count1 = cart_dict[sku_id]
            count0 = count1 + count
            # if count0 > 5:
            #     count0 = 5
            cart_dict[sku_id] = count0

        # 如果商品不存在，则添加数量偶倒购物车中
        else:
            cart_dict[sku_id] = count


        total_count = 0
        for k,v in cart_dict.items():
            total_count += v

        # 将字典专程字符串，存入cookies
        cart_str = json.dumps(cart_dict)
        response = JsonResponse({'status':1,'total_count':total_count})

        # 写入cookie
        response.set_cookie('cart',cart_str,expires=60*60)

    return response

def index(request):
    sku_list = []

    if request.user.is_authenticated():
        # 如果登录从ｒｅｄｉｓ中读取信息
        redis_client = get_redis_connection()
        key = 'cart%d'%request.user.id
        id_list = redis_client.hkeys(key)
        for id1 in id_list:
            sku = GoodsSKU.objects.get(pk=id1)
            sku.cart_count = int(redis_client.hget(key,id1))
            sku_list.append(sku)
        pass
    else:

        # 如果未登录从ｃｏｏｋｉｅ中读取信息
        cart_str = request.COOKIES.get('cart')

        # 判断购物车中是否有数据，如果有将购物车中的信息转为字典
        if cart_str:
            cart_dict = json.loads(cart_str)
            # 遍历字典，根据商品编号查询商品对象
            for k,v in cart_dict.items():
                sku = GoodsSKU.objects.get(pk=k)
                #　定义一个属性
                sku.cart_count = v
                sku_list.append(sku)

    context = {
        'title':'购物车',
        'sku_list':sku_list,

    }
    return render(request,'cart.html',context)