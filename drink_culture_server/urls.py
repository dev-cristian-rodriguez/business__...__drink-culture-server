from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/advertisements/', include('apps.advertisements.urls')),
    path('api/v1/categories/', include('apps.categories.urls')),
    path('api/v1/products/', include('apps.products.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/favorites/', include('apps.favorites.urls')),
    path('api/v1/customer_data/', include('apps.customer_data.urls')),
]
