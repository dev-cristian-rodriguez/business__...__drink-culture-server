from django.urls import path

from .views import UserView, UserListView, CreateUserView

urlpatterns = [
    path('', view=UserListView.as_view(), name='user_list'),
    path('<int:id>/', view=UserView.as_view(), name='user'),
    path('create/', view=CreateUserView.as_view(), name='create_user'),
]
