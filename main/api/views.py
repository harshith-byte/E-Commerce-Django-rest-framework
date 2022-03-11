import email
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
# Create your views here.

@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'category':'/category-list/',
        'products-list':'/products-list/',
        'detail view':'/category-list/<str:pk>/',
        'selected_product':'/selected-product/<str:pk>/',
        'cart_item':'/cart_item/',
    }


    return Response(api_urls)

@api_view(['GET'])
def Category_list(request):
    categorys=category.objects.all()
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def object_list(request,pk):
    object=products.objects.filter(category_id=pk)
    serializer = ProductsSerializer(object, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    product=products.objects.all()
    serializer=ProductsSerializer(product, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def selected_products(request,pk):
    sp=products.objects.get(id=pk)
    serial = ProductsSerializer(sp, many=False)
    return Response(serial.data)

@api_view(['GET'])
def cart_item(request):

    c=Cart.objects.all()

    serial=CartSerializer(c, many=True)
    return Response(serial.data)

@api_view(['POST'])
def register_user(request):
    data=request.data
    if data["Password"]==data["confirm_password"]:
        User.objects.create(email=data['Email'],
         username=data['Username'], 
         password=data['Password'], 
         first_name=data['firstname'],
         last_name=data['lastname'])

        return Response({"message":"you have registered successfully"})


    return Response({"message":"your both password's doesn't match"})

@api_view(['POST'])
def login_user(request):
    data=request.data
    u=data['Username']
    p=data['Password']
    user = authenticate(username=u, password=p)
    if user is not None:
        return Response({"message":"user logged in successfully"})

    return Response({"message":"Username or Password is incorrect"})

@api_view(['GET'])
def user_data(request):
    User.objects.all()
    return Response(User)

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

