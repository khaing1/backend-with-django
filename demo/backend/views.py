from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.
from backend.models import Township,Restaurant,Menu
from backend.serializer import RestaurantSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def restaurant_list(request,township_id):
  # try:
    # print(township_id)
    restaurants=Restaurant.objects.filter(township=township_id)
    restaurant_dict={
      'restaurants':restaurants
    }
    # restaurant_serializer=RestaurantSerializer(restaurants,many=True)
    # return JsonResponse(restaurant_serializer.data, safe=False)
    return render(request,'restaurant.html',context=restaurant_dict)

@api_view(['GET'])
def restaurant_detail(request,pk):
  menus=Menu.objects.filter(restaurant=pk)
  context={'menus':menus}
  return render(request,'menu.html',context=context)
