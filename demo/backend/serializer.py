from rest_framework import serializers
from backend.models import Restaurant,Menu

class RestaurantSerializer(serializers.ModelSerializer):
  class Meta:
    model=Restaurant
    fields=('id','name','township_id')
    # lookup_field='pk'