from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Product
from .cart import Cart

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'index.html',context)

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("store")

def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("store")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("store")
