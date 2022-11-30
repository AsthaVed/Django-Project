from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path('about', views.about, name='about'),
    path('service_pizza', views.service_pizza, name='service_pizza'),
    path('service_burger', views.service_burger, name='service_burger'),
    path('service_others', views.service_others, name='service_others'),
    path('contact', views.contact, name='contact'),
]
