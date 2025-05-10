from django.db import models
from django.utils import timezone

from apps.users.models import Custom_User
from apps.products.models import Products

class Shopping_Cart(models.Model) :
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
