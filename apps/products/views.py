from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.products.models import Products


class ProductsView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # Include filter by url params 
        items = model_to_dict(Products.objects.all())
        print(items)
        
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

    def post(self, request):
        pass


class ProductsByCategoryView (APIView) :
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # Include filter by url params 
        # Only filter products of specific category
        
        category_id_example = 2
        items = model_to_dict(Products.objects.filter(category_id=category_id_example))
        print(items)
        
        
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
    
    
class ProductDetailView (APIView) : 
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        # Include filter by url params 
        product_id_example = 2
        item = model_to_dict(Products.objects.get(id=product_id_example))
        print(item)
        
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