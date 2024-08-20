from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.urls import reverse_lazy
from .models import Hotel, Room, Reservation
from .forms import ReservationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from datetime import date

class ReservationConfirmationView(LoginRequiredMixin,DetailView):

    model = Reservation
    template_name = 'reservation_confirmation.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        reservation = self.object

         # Calculate the number of nights for the reservation
        nights = (reservation.check_out_date - reservation.check_in_date).days
        room_price = reservation.room.price
        tax_rate = Decimal('0.17')

        # Calculate the total price including a 17% tax
        total_price = nights * room_price * (1 + tax_rate)  
        
         # Add the calculated values to the context
        context['nights'] = nights
        context['room_price'] = room_price
        context['total_price'] = total_price
        return context
    
class ReservationView(LoginRequiredMixin,FormView):

    template_name = 'reservation_form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('reservation_confirmation')

    def form_valid(self, form):

        cleaned_data = form.cleaned_data
        hotel = cleaned_data['hotel']
        room = cleaned_data['room']
        check_in_date = cleaned_data['check_in_date']
        check_out_date = cleaned_data['check_out_date']

        # Check if the dates are not in the past
        current_date = date.today()
        if check_in_date < current_date:
            return redirect('error_dates')

        # Check if the room belongs to the hotel
        if room.hotel != hotel:
            return redirect('error_room')

        # Check if the room is available for the selected dates
        def invalid_room(check_in_date, check_out_date, room):
            reservations = Reservation.objects.filter(
                room=room,
                check_in_date__lt=check_out_date,
                check_out_date__gt=check_in_date
            )
            if reservations.exists():
                return 'room_unavailable'
            return None
        
        # validate room availability
        room_error = invalid_room(check_in_date, check_out_date, room)
        if room_error:
            return redirect(room_error)

        # Successful reservation
        reservation = form.save()
        return redirect('reservation_confirmation', pk=reservation.pk)
    
class RoomDetailView(LoginRequiredMixin, DetailView):
    model = Room
    template_name = "room_detail.html"

class HotelDetailView(LoginRequiredMixin, DetailView):
    model = Hotel
    template_name = "hotel_detail.html"

class HotelsListView(LoginRequiredMixin, ListView):
    model = Hotel
    template_name = "hotels.html"

class HomePageView(TemplateView):
    template_name = "home.html"


class ErrorRoomView(LoginRequiredMixin,TemplateView):
    template_name = 'error_room.html'

class RoomUnavailableView(LoginRequiredMixin,TemplateView):
    template_name = 'room_unavailable.html'

class ErrorDatesView(LoginRequiredMixin,TemplateView):
    template_name = 'error_dates.html'



