from django.db import models
from django.utils import timezone

# Create your models here.
class Banners(models.Model):
    image = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)