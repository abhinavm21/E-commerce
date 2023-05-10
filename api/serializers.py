from django.contrib.admin.filters import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework.schemas.coreapi import serializers
from rest_framework.serializers import ModelSerializer
from Products.models import Product


class ProductSerializer(ModelSerializer):
    activation = serializers.BooleanField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_activation(self, data):
        months = timezone.now() - timezone.timedelta(days=60)   
        return data.created <= months

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email','date_joined')

class UserAddSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email','date_joined')
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True,required=False)
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email','date_joined')
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



