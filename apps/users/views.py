from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render


class CreateUserView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request) :


        content = dict(info = "Cristian")
        return render(request, "user.html", {"element": "Hola cristian"})
        # return Response(content)

    def post(self, request) :
        content = dict(Message = "User Created")

        print(request.data)
        User.objects.create_user(
            username=request.data['username'],
            email=request.data['email'],
            password=request.data['password'],
            is_superuser=True, is_staff=True
        ).save()

        return Response(content)



class UserListView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):

        content = User.objects.all()
        return Response(content)


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        # print(request.method)
        # print(request.auth)
        # print(request.META)
        # print(request.query_params)
        # print(request.data)

        userDetailed = model_to_dict(User.objects.get(id=request.user.id))

        try :
            del userDetailed['user_permissions']
            del userDetailed['password']
            del userDetailed['groups']
        except KeyError:
            pass

        content = userDetailed
        return Response(content)

    def put(self, request):
        pass
