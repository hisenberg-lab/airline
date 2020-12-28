from django.db import models

# Create your models here.
class User(models.Model):
    UID = models.AutoField(primary_key = True)
    FNAME = models.CharField(max_length = 30)
    LNAME = models.CharField(max_length = 30)
    EMAIL = models.EmailField(max_length = 100, unique = True)
    PHONE = models.CharField(max_length = 12, unique = True)

class Airline_Company(models.Model):
    CID = models.AutoField(primary_key = True)
    COMPANY_NAME = models.CharField(max_length = 100)

class AIRPLANE(models.Model):
    AIRPLANE_NUMBER = models.IntegerField(primary_key=True)
    MODEL = models.CharField(max_length = 10)
    SEAT_CAPACITY = models.IntegerField()
    cid = models.ForeignKey(Airline_Company, on_delete=models.CASCADE)

class AIRPORT(models.Model):
    AIRPORT_CODE = models.CharField(max_length = 5, unique = True, primary_key = True)
    AIRPORT_NAME = models.CharField(max_length = 100)
    CITY = models.CharField(max_length = 30)
    ZIP = models.IntegerField()
    STATE = models.CharField(max_length = 30)
    COUNTRY = models.CharField(max_length = 30)
class ACCESS(models.Model):
    airplane_number = models.ForeignKey(AIRPLANE, on_delete=models.CASCADE)
    airport_code = models.ForeignKey(AIRPORT, on_delete=models.CASCADE)

class FLIGHT_TRIP(models.Model):
    TRIP_ID = models.AutoField(primary_key =True)
    airplane_number = models.ForeignKey(AIRPLANE, on_delete=models.CASCADE)
    DEPART_TIME = models.DateTimeField()
    DESTINATION_AIRPORT = models.ForeignKey(AIRPORT, on_delete=models.CASCADE, related_name= 'destination')
    ARIVAL_TIME = models.DateTimeField()
    ARIVAL_AIRPORT = models.ForeignKey(AIRPORT, on_delete=models.CASCADE, related_name= 'arival')

class SEAT(models.Model):
    SEAT_NUMBER = models.AutoField(primary_key = True)
    CLASS = models.CharField(max_length = 10)
    AVAILABILITY = models.BooleanField()
    airplane_number = models.ForeignKey(AIRPLANE, on_delete=models.CASCADE)
class PASSENGER(models.Model):
    PID = models.AutoField(primary_key = True)
    FNAME = models.CharField(max_length = 30)
    LNAME = models.CharField(max_length = 30)
    PHONE = models.CharField(max_length = 12)
    seat_number = models.ForeignKey(AIRPLANE, on_delete=models.CASCADE)

class FARE(models.Model):
    trip_id = models.ForeignKey(FLIGHT_TRIP, on_delete=models.CASCADE)
    AMOUNT = models.FloatField(max_length = 6)
    DISCOUNT = models.FloatField(max_length = 6, default=0)
    TAX = models.FloatField(max_length = 6)
    CURRENCY = models.CharField(max_length = 4)
