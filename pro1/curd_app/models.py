from django.db import models


class Hostel(models.Model):
    type = [("2 SEATER", "2 seater"), ("3 SEATER", "3 seater"), ("4 SEATER", "4 seater")]
    name = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.CharField(max_length=30)
    room = models.CharField(max_length=20, choices=type, default=True)
    arrival_date = models.DateField()
    leave_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


