from django.db import models



class Cab(models.Model):
    cab_name = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    cab_type = models.CharField(max_length=20)
    car_number = models.CharField(max_length=20)
    price_per_km = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.cab_name


class Booking(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    pickup = models.CharField(max_length=200)
    drop = models.CharField(max_length=200)

    cab_type = models.CharField(max_length=50)

    assigned_cab = models.CharField(max_length=100, blank=True)
    driver_name = models.CharField(max_length=100, blank=True)
    car_number = models.CharField(max_length=20, blank=True)

    # NEW FIELD
    members = models.IntegerField(default=1)

    date = models.DateField()
    time = models.TimeField()

    status = models.CharField(max_length=20, default="Booked")

    def __str__(self):
        return self.name