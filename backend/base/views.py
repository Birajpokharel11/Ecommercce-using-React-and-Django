from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from  .products import products
from .serailizers import ProductSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    data = {
        "apartment": "Hoses",
        "cost": 112
    }

    return Response(data)
@api_view(['GET'])
def getProducts(request): 
    products = Product.objects.all() 
    serailizer = ProductSerializer(products, many=True)
    print('Hello',serailizer.data)
    return Response(serailizer.data)

@api_view(['GET'])
def getProduct(request, pk):
    print('Hello IK', pk)
    product = Product.objects.get(_id=pk)
    serailizer = ProductSerializer(product, many=False)

    # for i in products:
    #     if i['_id'] == pk:
    #         product = i 
    return Response(serailizer.data)




