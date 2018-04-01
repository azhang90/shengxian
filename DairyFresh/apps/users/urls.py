from django.conf.urls import include, url
from django.contrib import admin
from users import views

urlpatterns = [
    url('^register/$',views.RegisterView.as_view()),
    url('^active/(.+)$',views.active),
    url('^login$',views.LoginView.as_view()),
    url('^logout$',views.logout_user),
    url('^info$',views.info),
    url('^order$',views.order),
    url('^site$',views.SiteView.as_view()),
    url('^area$',views.area),
]
# http://127.0.0.1:8000/user/active/11
# http://127.0.0.1:8000/user/active/eyJleHAiOjE1MjE4ODkyMTQsImlhdCI6MTUyMTg4NTYxNCwiYWxnIjoiSFMyNTYifQ.eyJpZCI6OX0.lw9vP33uj0acemxalryKQDJfG8uTlHOeNjkZOWAPA74