#define Serializer class for User model
from django.contrib.auth.models import User
from .models import MenuItem, Reserva
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'inventory']

class BookingSerializers(serializers.ModelSerializer): 
    class Meta:
        model = Reserva
        fields = '__all__'