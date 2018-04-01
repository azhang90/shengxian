# coding=utf-8
from django.views.generic import View
from django.contrib.auth.decorators import login_required


class LoginRequiredViewMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        #通用视图的as_view()是通过请求方式获得视图函数
        func = super().as_view(**initkwargs) #as_view得出请求方式
        return login_required(func) #给的出的请求方式加上判断是否登录的装饰器