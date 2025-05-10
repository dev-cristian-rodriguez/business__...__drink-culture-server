from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.categories.models import Categories

class CategoriesView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        items = model_to_dict(Categories.objects.all())
        print(items)
        
        
        content = dict(status="200", data="response with success")
        return Response(content)