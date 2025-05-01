from django.db import models
from django.utils import timezone

from apps.users.models import Users
from apps.products.models import Products

class ShoppingCart(models.Model) :
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
