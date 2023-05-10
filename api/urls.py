from django.urls import path
from . import views


urlpatterns=[
        path('',views.intro),
        path('products',views.all_products),
        path('product/<int:pk>',views.product),
        path('create-product',views.create_product),
        path('update-product/<int:pk>',views.update_product),
        path('delete-product/<int:pk>',views.delete_product),
        path('customers',views.all_customers),
        path('customer/<int:pk>',views.customer),
        path('customer-products/<int:pk>',views.customer_products),
        path('create-customer',views.create_customer),
        path('update-customer/<int:pk>',views.update_customer),
        path('delete-customer/<int:pk>',views.delete_customer),
        ]

