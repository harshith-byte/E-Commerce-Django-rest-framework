from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('categories/', views.categories, name="categories"),

    path('categories/<int:pk>/', views.categoryproduct, name="categoryproduct"),
  
    path('logout', LogoutView.as_view(), name="logout"),

    path('product/<int:pk>/',views.product, name='product'),

    path('cart/', views.cart, name="cart"),

    path('cart/<int:pk>', views.cart_add, name="cart_add"),

    path('login/',views.login,name="login"),

    path('register/',views.register,name="register")
]