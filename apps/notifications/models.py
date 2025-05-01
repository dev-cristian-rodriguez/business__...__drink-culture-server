from django.db import models
from django.utils import timezone

from apps.users.models import Users


class Notifications(models.Model) :
    title = models.CharField(max_length=200)
    description = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
