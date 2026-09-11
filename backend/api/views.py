from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from products.serializers import ProductSerializer
from django.forms.models import model_to_dict
from products.models import Product



@api_view(['POST']) #we have to declare what methods we allow
def api_home(request):
    ''' DRF API View '''


    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        data = serializer.save()
    return Response(serializer.data)