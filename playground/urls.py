from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/add/', views.cart_add, name='cart_add'),
    #path('cart/increment/<id>/', views.item_increment, name='item_increment'),
    path('cart/decrement/', views.item_decrement, name='item_decrement')
]