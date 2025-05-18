from django.urls import path

from .views import UserView, UserListView, CreateUserView, GoogleLogin

urlpatterns = [
    path('', view=UserListView.as_view(), name='user_list'),
    path('login-google/', view=GoogleLogin.as_view(), name='google_login'),
    path('<int:id>/', view=UserView.as_view(), name='user'),
    path('create/', view=CreateUserView.as_view(), name='create_user'),
]
