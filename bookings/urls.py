from django.urls import path
from django.conf.urls import url
from . import views
from .views import book

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('result/', views.search, name = 'result'),
    path('book/', book.as_view(), name = 'book'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('payment/', views.payment, name = 'payment'),
    path('trip/<tripId>', views.trip, name= 'trip')

]