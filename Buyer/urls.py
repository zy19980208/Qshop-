
from django.urls import path,include,re_path
from Buyer.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    # path('Saller/',include('Saller.urls')),
    path('login/',login),
    path('index/',index),
    path('register/',register),
    path('base/',base),
    path('logout/',logout),
    # path('goods_list/',cache_page(60*15)(goods_list)),
    path('goods_list/',goods_list),
    re_path('goods_list/(?P<page>\d+)',goods_list),
    re_path('detail/(?P<id>\d+)',detail),
    path('user_center_info/',user_center_info),
    path('user_center_order/',user_center_order),
    path('place_order/',place_order),
    path('place_order_more/',place_order_more),
    path('alipayviews/',AlipayViews),
    path('payresult/',payresult),
    path('add_cart/',add_cart),
    path('cart/',cart),
    # path('cache_test/',cache_test),
    path('reqtest/',reqtest),
    path('process_tem_rep/',process_tem_rep),

]