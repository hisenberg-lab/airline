from django.contrib import admin

# Register your models here.

from .models import User, Airline_Company, AIRPLANE, AIRPORT, ACCESS, FLIGHT_TRIP, SEAT, PASSENGER, FARE

admin.site.register(User)
admin.site.register(Airline_Company)
admin.site.register(AIRPLANE)
admin.site.register(AIRPORT)
admin.site.register(ACCESS)
admin.site.register(FLIGHT_TRIP)
admin.site.register(SEAT)
admin.site.register(PASSENGER)
admin.site.register(FARE)