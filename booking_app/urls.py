from django.urls import path
from .views import HomePageView, HotelsListView, HotelDetailView, RoomDetailView, ReservationView, ReservationConfirmationView, ErrorRoomView, RoomUnavailableView, ErrorDatesView
from .rest_views import HotelListApiView,RoomListApiView,HotelSearchAPIView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hotels/', HotelsListView.as_view(), name='hotels'),
    path('hotel/<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('reserve/', ReservationView.as_view(), name='reserve'),
    path('error_room/', ErrorRoomView.as_view(), name='error_room'),
    path('room_unavailable/', RoomUnavailableView.as_view(), name='room_unavailable'),
    path('error_dates/', ErrorDatesView.as_view(), name='error_dates'),
    path('reservation/confirmation/<int:pk>/', ReservationConfirmationView.as_view(), name='reservation_confirmation'),

    path('api/hotels/', HotelListApiView.as_view(http_method_names=['get'])),
    path('api/rooms/', RoomListApiView.as_view(http_method_names=['get'])),

    path('api/hotel/',HotelListApiView.as_view(http_method_names=['post'])),
    path('api/room/',RoomListApiView.as_view(http_method_names=['post'])),

    path('api/hotel-search/', HotelSearchAPIView.as_view(), name='hotel-search'),   
]
