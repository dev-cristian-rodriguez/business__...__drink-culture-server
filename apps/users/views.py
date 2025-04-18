from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from django.forms.models import model_to_dict

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