# booking/views.py
from django.shortcuts import render
from .models import Master, Service

def home(request):
    return render(request, 'home.html')

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'master_list.html', {'masters': masters})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def about_us(request):
    return render(request, 'about_us.html')

def book_appointment(request):
    return render(request, 'book_appointment.html')
