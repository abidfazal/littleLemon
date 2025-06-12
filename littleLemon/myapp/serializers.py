from rest_framework import serializers
from .models import Menu,Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', 'inventory']
        
class BookingSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'booking_date', 'no_of_guests']
        
        
        