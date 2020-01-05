from django.db import models
from django import forms

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.car_name,filename)


class CarType(models.Model):
    Car = 'C'
    Truck = 'T'
    CarryVan = 'CV'

    CAR_TYPE_CHOICES = [
        (Car, 'C'),
        (Truck, 'T'),
        (CarryVan, 'CV')
    ]

    CarType_Choices = models.CharField(
        max_length=2,
        choices=CAR_TYPE_CHOICES,
        default=Car,
    )
    def is_upperclass(self):
        return self.CarType_Choices in {self.Truck, self.CarryVan}

class Car(models.Model):
    image = models.ImageField(upload_to=uploaded_location,null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    car_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    num_of_seats = models.IntegerField()
    num_of_bed = models.IntegerField(default=0)
    cost_par_day = models.CharField(max_length=50)
    cost_per_week = models.CharField(max_length=50)
    weekend_cost = models.CharField(max_length=50)
    plate_number = models.CharField(max_length=50)
    weekend_cost = models.CharField(max_length=50)
    avaliable = models.BooleanField(default=False)
    content = models.TextField()
    like = models.IntegerField(default=0)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class Order(models.Model):
    car_name = models.CharField(max_length=100)
    employee_name = models.CharField(max_length=100)
    cell_no = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField()
    to = models.DateTimeField()

    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)

class PrivateMsg(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
