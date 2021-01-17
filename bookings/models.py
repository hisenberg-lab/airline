from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     UID = models.AutoField(primary_key = True)
#     FNAME = models.CharField(max_length = 30)
#     LNAME = models.CharField(max_length = 30)
#     EMAIL = models.EmailField(max_length = 100, unique = True)
#     PHONE = models.CharField(max_length = 12, unique = True)

GENDER = (
    ("M","MALE"),
    ("F", "FEMALE")
)

seat_class = (
    ("F","FIRST"),
    ("B", "BUSINESS"),
    ("E", "ECONOMY")
)    

class USER_INFO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 13)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    DISCOUNT = models.FloatField(default=0)
class Airline_Company(models.Model):
    CID = models.AutoField(primary_key = True)
    COMPANY_NAME = models.CharField(max_length = 100)

class AIRPLANE(models.Model):
    AIRPLANE_NUMBER = models.IntegerField(primary_key=True)
    MODEL = models.CharField(max_length = 10)
    SEAT_CAPACITY = models.IntegerField()
    cid = models.ForeignKey(Airline_Company,to_field= 'CID', on_delete=models.CASCADE)

class AIRPORT(models.Model):
    AIRPORT_CODE = models.CharField(max_length = 5, unique = True, primary_key = True)
    AIRPORT_NAME = models.CharField(max_length = 100)
    CITY = models.CharField(max_length = 30)
    ZIP = models.IntegerField()
    STATE = models.CharField(max_length = 30)
    COUNTRY = models.CharField(max_length = 30)
class ACCESS(models.Model):
    airplane_number = models.ForeignKey(AIRPLANE,to_field= 'AIRPLANE_NUMBER', on_delete=models.CASCADE)
    airport_code = models.ForeignKey(AIRPORT,to_field= 'AIRPORT_CODE', on_delete=models.CASCADE)

class FLIGHT_TRIP(models.Model):
    TRIP_ID = models.AutoField(primary_key =True)
    airplane_number = models.ForeignKey(AIRPLANE,to_field= 'AIRPLANE_NUMBER', on_delete=models.CASCADE)
    DEPART_TIME = models.DateTimeField()
    DEPARTURE_AIRPORT = models.ForeignKey(AIRPORT,to_field= 'AIRPORT_CODE', on_delete=models.CASCADE, related_name= 'destination')
    ARIVAL_TIME = models.DateTimeField()
    ARIVAL_AIRPORT = models.ForeignKey(AIRPORT,to_field= 'AIRPORT_CODE', on_delete=models.CASCADE, related_name= 'arival')

class SEAT(models.Model):
    id = models.AutoField(primary_key = True)
    FIRST = models.IntegerField(default=0)
    ECONOMY = models.IntegerField(default=0)
    BUSINESS = models.IntegerField(default=0)
    airplane_number = models.ForeignKey(AIRPLANE, to_field= 'AIRPLANE_NUMBER', on_delete=models.CASCADE)
    trip_id = models.ForeignKey(FLIGHT_TRIP, to_field="TRIP_ID", on_delete=models.CASCADE)
    class Meta:
        unique_together = ("id", "trip_id")
        # constraints =[ models.CheckConstraint(check = AIRPLANE.objects.get(AIRPLANE_NUMBER = airplane_number).SEAT_CAPACITY >= FIRST+ECONOMY+BUSINESS)]
class PASSENGER(models.Model):
    PID = models.AutoField(primary_key = True)
    FNAME = models.CharField(max_length = 30)
    LNAME = models.CharField(max_length = 30)
    PHONE = models.CharField(max_length = 15)
    airplane_number = models.ForeignKey(AIRPLANE,to_field= 'AIRPLANE_NUMBER', on_delete=models.CASCADE)
    # seat_number = models.ForeignKey(SEAT, on_delete=models.CASCADE)
    trip_id = models.ForeignKey(FLIGHT_TRIP,to_field= 'TRIP_ID', on_delete=models.CASCADE)
    SEX = models.CharField(choices = GENDER ,max_length = 1)
    CLASS = models.CharField(choices = seat_class, max_length = 1)
    user = models.ForeignKey(USER_INFO, to_field="user" , on_delete=models.RESTRICT)

class FARE(models.Model):
    trip_id = models.ForeignKey(FLIGHT_TRIP,to_field= 'TRIP_ID', on_delete=models.CASCADE)
    AMOUNT = models.FloatField(max_length = 6)
    DISCOUNT = models.FloatField(max_length = 6, default=0)
    TAX = models.FloatField(max_length = 6)
    CURRENCY = models.CharField(max_length = 4, default = 'INR')

#TABLE UPDATED ONLY BY TRIGGER
class TRANSACTION(models.Model):
    user = models.ForeignKey(USER_INFO, to_field="user" , on_delete=models.CASCADE)
    date = models.DateTimeField()
    trip_id = models.ForeignKey(FLIGHT_TRIP,to_field= 'TRIP_ID', on_delete=models.SET_NULL, null = True)
