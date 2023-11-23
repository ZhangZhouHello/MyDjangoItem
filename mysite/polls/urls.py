from django.urls import path
from . import views

urlpatterns = [
    # 前面是拼接路由地址 views.toLogin_view 代表引用toLogin_view这个方法
    path('', views.toLogin_view, name='toLogin'),
]