from django.db import models
from django.utils import timezone

from apps.users.models import Custom_User
from apps.products.models import Products

class Customer_Address(models.Model):
    full_name = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    physical_address = models.CharField(max_length=1000)
    additional_references = models.CharField(max_length=1000, null=True)
    user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Customer_Orders(models.Model) :
    status = models.IntegerField()
    user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer_address_id = models.ForeignKey(Customer_Address, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Customer_Payments(models.Model) :
    payment_type = models.IntegerField()
    provider = models.IntegerField()
    expiration_date = models.DateField()
    user_id = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

