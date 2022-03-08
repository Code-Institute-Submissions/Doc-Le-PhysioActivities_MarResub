from cProfile import label
import uuid
from datetime import datetime
from django.db import models
from services.models import Clinician, Service
from user.models import User

class BookingDate(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

class BookingTime(models.Model):
    time = models.TimeField()
   
    def __str__(self):
        return self.time.strftime("%H:%M")

class Booking(models.Model):
    booking_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, null=False, blank=False, on_delete=models.CASCADE) 
    date = models.ForeignKey(BookingDate, null=False, blank=False, on_delete=models.CASCADE)
    time = models.ForeignKey(BookingTime, null=False, blank=False, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        
        self.datetime = datetime.combine(self.date, self.time)
        self.total = self.service.price
        super().save(*args, **kwargs)

    def _generate_booking_number(self):
        """
        Generate a random, unique booking number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.booking_number