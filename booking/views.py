
from django.shortcuts import render

# Create your views here.

from .models import Master, Service

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'booking/master_list.html', {'masters': masters})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'booking/service_list.html', {'services': services})