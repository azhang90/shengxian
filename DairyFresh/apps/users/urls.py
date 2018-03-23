from django.conf.urls import include, url
from django.contrib import admin
from users import views

urlpatterns = [
    url('^register$',views.register)
]
