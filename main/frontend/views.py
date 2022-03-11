from statistics import quantiles
from tkinter import PROJECTING
from django.shortcuts import render
import os
from django.conf import settings
from django.shortcuts import render
from django.templatetags.static import static
from api.views import *
from api.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
def mainpage(request):

    return render(request, 'frontend/mainpage.html')

def categories(request):
    ob=category.objects.all()
    content={'ob':ob}
    return render(request, 'frontend/categories.html',content)


def categoryproduct(request,pk):
    ob=category.objects.get(id=pk)
    content={'ob':ob}
    return render(request, 'frontend/categoryproduct.html',content)


def product(request,pk):
    ob=products.objects.get(id=pk)
    content={'ob':ob}
    return render(request, 'frontend/product.html', content)

def cart(request):
    return render(request, 'frontend/cart.html')

@api_view(['POST'])
def cart_add(request):
    data=request.data
    if User.is_authenticated():
        Cart.objects.create(
            product=data["product_id"],
            user=User.id,
            quantity=1,
        )
        return render(request, 'frontend/cart.html')

def login(request):
    return render(request,'frontend/login.html')

def register(request):
    return render(request,'frontend/register.html')