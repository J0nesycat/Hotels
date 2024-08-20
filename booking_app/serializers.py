from rest_framework import serializers
from .models import Hotel, Room 


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model= Room
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):

    rooms = RoomSerializer(read_only=True, many=True)

    class Meta:
        model= Hotel
        fields = ["title","stars","location","rooms"]


class RoomAvailabilitySearch(serializers.Serializer):
    check_in_date = serializers.DateField()
    check_out_date = serializers.DateField()