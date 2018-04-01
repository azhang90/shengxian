from django.conf.urls import include, url
from django.contrib import admin
from . import views
import haystack.urls



urlpatterns = [
    url('^fdfs_test$',views.fdfs_test),
    url('^index$',views.index),
    url(r'^(\d+)$',views.detail),
    url(r'^list(\d+)$',views.list_sku),
    url(r'^search/$', views.MySearchView.as_view()),
]
