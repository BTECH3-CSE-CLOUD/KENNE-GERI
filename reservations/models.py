from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()

    def __str__(self):
        return f"Reservation by {self.user.username} for Table {self.table.number} on {self.date} at {self.time}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Reservation {self.reservation.id}"
