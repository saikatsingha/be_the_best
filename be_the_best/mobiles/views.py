from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.db import models

from mobiles.models import Product_details, Product_type
from mobiles.serializers import Product_type_Serializers, Product_details_Serializers

# Create your views here.

@csrf_exempt
def mobilesApi(request):
    mobiles = Product_details.objects.all()
    mob_serializers = Product_details_Serializers(mobiles, many=True)
    return JsonResponse(mob_serializers.data, safe=False)