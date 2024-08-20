from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hotel,Room,Reservation
from .serializers import HotelSerializer,RoomSerializer,RoomAvailabilitySearch
from datetime import date, datetime

class HotelSearchAPIView(APIView):
    def get(self, request, *args, **kwargs):

        # get the check-in and check-out dates from the query parameters
        check_in_date = request.query_params.get('check_in_date')
        check_out_date = request.query_params.get('check_out_date')

        # check if both dates are provided, if not, return an error response
        if not check_in_date or not check_out_date:
            return Response({"error": "Missing dates"}, status=status.HTTP_400_BAD_REQUEST)

        # convert the date strings to date objects
        #solution for TypeError: '<' not supported between instances of 'str' and 'datetime.date'
        try:
            check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        
        # validate the dates: check-in date must be in the future and check-out date must be after check-in date
        if check_in_date < date.today() or check_out_date <= check_in_date:
            return Response({"error": "Invalid dates"}, status=status.HTTP_400_BAD_REQUEST)
        
        # get all hotels from the database
        available_hotels = Hotel.objects.all()
        available_hotels_with_rooms = []

        #get through each hotel to check for available rooms
        for hotel in available_hotels:
            #exclude rooms that are already reserved within the given date range
            available_rooms = hotel.rooms_as_foreign_key.exclude(
                id__in=Reservation.objects.filter(
                    check_in_date__lt=check_out_date,
                    check_out_date__gt=check_in_date
                ).values_list('room_id', flat=True)
            )
            # If the hotel has available rooms, serialize the hotel and room data
            if available_rooms.exists():
                hotel_serializer = HotelSerializer(hotel)
                hotel_data = hotel_serializer.data
                hotel_data['rooms'] = RoomSerializer(available_rooms, many=True).data
                available_hotels_with_rooms.append(hotel_data)

         # return response
        return Response(available_hotels_with_rooms, status=status.HTTP_200_OK)

class HotelListApiView(APIView):

    def get(self,request):
        list_of_hotels = Hotel.objects.all()
        serializer = HotelSerializer(list_of_hotels, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):

        data = {
            'title': request.data.get('title'),
            'stars': request.data.get('stars'),
            'location': request.data.get('location'),
            'rooms' : request.data.get('rooms')
        }

        hotel= HotelSerializer(data=data)

        if hotel.is_valid():
            hotel.save()
            return Response(hotel.data, status=status.HTTP_201_CREATED)
        
        return Response(hotel.errors, status=status.HTTP_400_BAD_REQUEST)




class RoomListApiView(APIView):

    def get(self,request):

        list_of_rooms = Room.objects.all()
        serializer = RoomSerializer(list_of_rooms, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        data = {
            'title': request.data.get('title'),
            'room_number': request.data.get('room_number'),
            'number_of_guests': request.data.get('number_of_guests'),
            'price': request.data.get('price'),
            'size': request.data.get('size'),
            'hotel':request.data.get('hotel'),

        }

        room= RoomSerializer(data=data)
        
        if room.is_valid():
            room.save()
            return Response(room.data, status=status.HTTP_201_CREATED)
        
        return Response(room.errors, status=status.HTTP_400_BAD_REQUEST)

