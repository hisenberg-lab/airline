from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from bookings.forms import UserForm, UserProfileInfoForm, passengerSet
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from bookings.models import AIRPORT, USER_INFO, Airline_Company, AIRPLANE, AIRPORT, ACCESS, FLIGHT_TRIP, SEAT, PASSENGER, FARE

# Create your views here.
def index(request):
    airport = AIRPORT.objects.all()
    return render(request,'bookings/index.html', {'airports' : airport})


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'bookings/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'bookings/login.html', {})

def payment(request):
    return render(request,'bookings/payment.html')

@login_required
def search(request):
    if request.method == 'POST':
        fromPlace = request.POST.get('from')
        toPlace = request.POST.get('to')
        oneWay = request.POST.get('one-way')
        roundTrip = request.POST.get('round-trip')
        departure = request.POST.get('departure-date')
        returnDate = request.POST.get('return-date')
        travellers = request.POST.get('number-of-travellers')
        seatClass = request.POST.get('class')
        print(fromPlace,toPlace,oneWay,roundTrip,departure,returnDate,travellers,seatClass)

        flightTrip = FLIGHT_TRIP.objects.filter(DEPARTURE_AIRPORT__exact = fromPlace , ARIVAL_AIRPORT__exact = toPlace, )
        
        if oneWay == '1':
            flightTrip = flightTrip.select_related('airplane_number').filter(DEPART_TIME__date = departure).values()
            airplanes = flightTrip.values_list('airplane_number','TRIP_ID')
            airports = flightTrip.values_list('DEPARTURE_AIRPORT','ARIVAL_AIRPORT')
            if flightTrip and airplanes != None:
                airplane_number, trip_id= zip(*airplanes)
                depart, arival = zip(*airports)
                seat = SEAT.objects.filter(airplane_number__in = airplane_number, trip_id__in = trip_id)
                fare = FARE.objects.filter(trip_id__in = trip_id)
                departAirport = AIRPORT.objects.filter(AIRPORT_CODE__in = depart)
                arivalAirport = AIRPORT.objects.filter(AIRPORT_CODE__in = arival)
                # print(flightTrip.values(), seat.values(), fare.values())
                content = {
                    'planes' : zip(flightTrip.values(), seat.values(), fare.values(), departAirport.values(), arivalAirport.values())
                }
                return render(request, "bookings/result.html", content)
            else:
                return render(request, "bookings/result.html", {'available' : False})
        elif roundTrip == '2':
            flightTrip = flightTrip.select_related('airplane_number').filter(DEPART_TIME__date = departure, ARIVAL_TIME__date = returnDate).values()
            airplanes = flightTrip.values_list('airplane_number','TRIP_ID')
            airports = flightTrip.values_list('DEPARTURE_AIRPORT','ARIVAL_AIRPORT')
            # print(depart)
            if flightTrip and airplanes != None:
                airplane_number, trip_id= zip(*airplanes)
                depart, arival = zip(*airports)
                seat = SEAT.objects.filter(airplane_number__in = airplane_number, trip_id__in = trip_id)
                fare = FARE.objects.filter(trip_id__in = trip_id)
                departAirport = AIRPORT.objects.filter(AIRPORT_CODE__in = depart)
                arivalAirport = AIRPORT.objects.filter(AIRPORT_CODE__in = arival)
                # print(flightTrip.values(), seat.values(), fare.values(), departAirport.values(), arivalAirport.values())
                content = {
                    'planes' : zip(flightTrip.values(), seat.values(), fare.values(), departAirport.values(), arivalAirport.values())
                }
                return render(request, "bookings/result.html", content)
            else:
                return render(request, "bookings/result.html", {'available' : False})
    return HttpResponseRedirect(reverse('index'))

@login_required
def trip(request,tripId):
    request.session["tasks"] = tripId
    return HttpResponseRedirect(reverse('book'))

# @login_required
class book(TemplateView):
    #    if request.method == 'POST':
    template_name = "bookings/book.html"
    def get(self, *args, **kwargs):
        formset = passengerSet(queryset = PASSENGER.objects.none())
        return self.render_to_response({'passenger_set':formset})

    def post(self, *args, **kwargs):
        formset = passengerSet(data=self.request.POST)
        if formset.is_valid():
            if formset.cleaned_data != {}:
                p = formset.cleaned_data
        
            # d =formset.deleted_forms
            print(p)
            return HttpResponseRedirect(reverse("payment"))
        return self.render_to_response({'passenger_set': formset})