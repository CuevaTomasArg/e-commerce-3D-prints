from django.shortcuts import render,redirect
from .models import *
from .Cart import *
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'shop.html',{"products":products})

def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product)
    return redirect("shop")

def delete_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete(product)
    return redirect("shop")

def substract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("shop")

def clean_up_cart(request):
    cart = Cart(request)
    cart.clean_up()
    return redirect("shop")

