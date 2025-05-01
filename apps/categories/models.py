from django.db import models
from django.utils import timezone


class Categories(models.Model) :
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
