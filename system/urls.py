from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.home),

     url(r'^carlist/$', views.car_list,name = "car_list"),
    url(r'^createOrder/$', views.order_created),

    url(r'^(?P<id>\d+)/edit/$', views.car_update),


    url(r'^(?P<id>\d+)/$', views.car_detail),
    url(r'^detail/(?P<id>\d+)/$',views.order_detail),

    url(r'^(?P<id>\d+)/delete/$', views.car_delete),
    url(r'^(?P<id>\d+)/deleteOrder/$',views.order_delete),

    url(r'^contact/$', views.contact),

    url(r'^newcar/$',views.newcar),
    url(r'^(?P<id>\d+)/like/$', views.like_update),
    url(r'^popularcar/$',views.popular_car),

]
