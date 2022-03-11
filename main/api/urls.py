from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.apioverview,name="api-overview"),
    path('category-list/',views.Category_list,name="category-list"),
    path('product-list/',views.product_list,name="product-list"),
    path('category-list/<str:pk>/',views.object_list,name="object-list"),
    path('selected-product/<str:pk>/', views.selected_products, name="selected_products"),
    path('cart_item/', views.cart_item, name="cart_item"),
    path('registeruser/', views.register_user, name="registeruser"),
    path('loginuser/', views.login_user, name="loginuser"),
    path('userdata/', views.user_data, name="userdata"),
]