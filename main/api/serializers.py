
from rest_framework import serializers

from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=products
        fields = '__all__'
    
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields = '__all__'



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
    # def create(self, validated_data):
    # # Once the request data has been validated, we can create a todo item instance in the database
    #     return Cart.objects.create(
    #     obj_id=validated_data.get('obj_id')
    #     )