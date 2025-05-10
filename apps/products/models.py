from django.db import models
from django.utils import timezone

from apps.categories.models import Categories


class Products (models.Model) :
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_prince = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
