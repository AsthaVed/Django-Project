from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # messages.success(request, 'this is a text msg!')
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def service_pizza(request):
    return render(request, 'service_pizza.html')
def service_burger(request):
    return render(request, 'service_burger.html')
def service_others(request):
    return render(request, 'service_others.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')