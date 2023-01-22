from django.shortcuts import render,redirect
from .models import *
from .forms import SingUpForm
from .Cart import *
import pandas
import datetime

from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView,UpdateView
from django.contrib.auth.views import LoginView, LogoutView


# Create your views here.
def index(request):
    products = Product.objects.all()
    customizable = Category.objects.filter(name__contains = "Personalizable")
    customizables =Product.objects.filter(category_id = customizable.first().id)
    best_product = Category.objects.filter(name__contains = "Mas vendido")
    best_products = Product.objects.filter(category_id = best_product.first().id)
    return render(request, 'index.html',{"products":products,"customizables":customizables,"best_products":best_products})

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

# class SingUp(CreateView):
#     pass
#     # form_class = SingUpForm
#     # success_url = '/'
#     # template_name = 'singup.html'

# class AdminLoginView(LoginView):
#     pass
#     # template_name = 'login.html'
    
# class AdminLogoutView(LogoutView):
#     pass
#     # template_name = 'logout.html'
