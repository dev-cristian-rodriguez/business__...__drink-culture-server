from django.db import models
from django.utils import timezone


class Categories(models.Model) :
    name = models.CharField(max_length=60)
    description = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
