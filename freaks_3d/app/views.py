from django.shortcuts import render,redirect
from .models import *
from .Cart import *
import pandas
import datetime
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{"products":products})

def products(request):
    return render(request, 'products.html', {"products": Product.objects.all()})

def customizable(request):
    return render(request, 'customized.html', {"customizable":Customizable.objects.all()})

def filament(request,brand):
    category = Category.objects.get(brand=brand)
    return render(request, 'filament.html', {"filament":Product.objects.get(category_id=category.id),"brand":brand})

def contact(request):
    return render(request, 'contact.html')
    
def add_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.add(product)
    return redirect("index")

def delete_product(request,product_id):
    cart = Cart(request)
    product = Product.objects.get(id = product_id)
    cart.delete(product)
    return redirect("index")

def substract_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product)
    return redirect("index")

def clean_up_cart(request):
    cart = Cart(request)
    cart.clean_up()
    return redirect("index")

