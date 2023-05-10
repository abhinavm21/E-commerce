from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Products.models import Product
from .serializers import ProductSerializer, UserAddSerializer, UserSerializer, UserUpdateSerializer

@api_view(['GET'])
def intro(request):
    routes = [
            'GET /api',
            'GET /api/products',
            'GET /api/products/<int:pk>',
            'GET /api/create-product',
            'GET /api/update-product/<int:pk>',
            'GET /api/delete-product/<int:pk>',
            'GET /api/customers',
            'GET /api/customer/<int:pk>'
            'GET /api/create-customer',
            'GET /api/update-customer/<int:pk>',
            'GET /api/delete-customer/<int:pk>',
            ]
    return Response(routes)

# Product CRUD Area
@api_view(['GET'])
def all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create_product(request):
    data = request.data
    serializer = ProductSerializer(data=data,many=False)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        return Response(serializer.data)
    #if user.

@api_view(['PUT'])
def update_product(request,pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response({"Message": "Your item is deleted"})


# Customer CRUD Area
@api_view(['GET'])
def all_customers(request):
    customer = User.objects.filter(is_staff=False)
    serializer = UserSerializer(customer, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def customer(request,pk):
    customer = User.objects.get(id=pk)
    serializer = UserSerializer(customer, many=False)
    return Response(serializer.data)

@api_view(['GET']) 
def customer_products(request,pk):
    customer = Product.objects.filter(user=pk)
    serializer = ProductSerializer(customer, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_customer(request):
    data = request.data
    serializer = UserAddSerializer(data=data,many=False)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        return Response(serializer.data)
    #if user.

@api_view(['PUT'])
def update_customer(request,pk):
    customer = User.objects.get(id=pk)
    serializer = UserUpdateSerializer(instance=customer, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_customer(request,pk):
    product = User.objects.get(id=pk)
    product.delete()

    return Response({"Message": "Your item is deleted"})

