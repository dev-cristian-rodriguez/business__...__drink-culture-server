from django.db import models
from django.utils import timezone

from apps.users.models import Custom_User


class Notifications(models.Model) :
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
