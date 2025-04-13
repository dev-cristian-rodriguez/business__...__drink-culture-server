from django.urls import path

# Endpoints for user-related operations 
from views import home

urlpatterns = [
    path('', home, name='home'),
]