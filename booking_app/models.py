from django.db import models
from django.urls import reverse
import uuid

class Reservation(models.Model):

    full_name = models.CharField(max_length=255)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    confirmation_number = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def __str__(self):
        return f'Reservation for {self.full_name} in room {self.room.title} of hotel {self.hotel.title}'
    
    # override the save method to generate a unique confirmation number if it doesn't exist
    def save(self, *args, **kwargs):
        if not self.confirmation_number:
            self.confirmation_number = str(uuid.uuid4())
        super().save(*args, **kwargs)

class Hotel(models.Model):
    
    title = models.TextField()
    stars = models.TextField()
    location = models.TextField()
    rooms = models.ManyToManyField('Room', related_name='hotels')

    def get_absolute_url(self):
        return reverse('hotel_detail', kwargs={'pk': self.pk})    

    def __str__(self):
        return self.title[:20]

    def get_room_count(self):
        return self.rooms.count()

class Room(models.Model):

    title = models.TextField()
    room_number = models.IntegerField(unique=True)
    number_of_guests = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    size = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms_as_foreign_key', null=True)

    def get_absolute_url(self):
        return reverse('room_detail', kwargs={'pk': self.pk})    

    def __str__(self):
        return self.title[:20]
