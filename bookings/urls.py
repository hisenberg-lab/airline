from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('result/', views.search, name = 'result'),
    path('book/', views.book, name = 'book'),
    path('user_login/', views.user_login, name = 'user_login'),
    path('payment/', views.payment, name = 'payment')

]