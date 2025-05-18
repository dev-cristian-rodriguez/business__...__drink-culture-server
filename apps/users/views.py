from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import render

from rest_framework_simplejwt.tokens import RefreshToken


# Services
from apps.users.services import google_get_access_token, google_get_user_info


class GoogleLogin(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        if not request.data.get('code'):
            return Response({"error": "code not found"}, status=400)
        
        access_token = google_get_access_token(request.data.get('code'))
        user_data = google_get_user_info(access_token=access_token)
        
        u = User.objects.get(email=user_data['email'])
        
        if not u :
            new_user = User.objects.create_user(
                email=user_data['email'],
                full_name=user_data['name'],
                is_active=True,
                is_superuser=False,
                is_staff=False,
            )
            new_user.save()
            
            refresh = RefreshToken.for_user(new_user)
            access_token = str(refresh.access_token)
            
            return Response({
                "access_token": access_token,
                "refresh_token": str(refresh),
            })
            
        else :
            refresh = RefreshToken.for_user(u)
            access_token = str(refresh.access_token)
            
            return Response({
                "access_token": access_token,
                "refresh_token": str(refresh),
            })
            

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
