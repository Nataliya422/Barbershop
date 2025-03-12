from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Master, Service

admin.site.register(Master)
admin.site.register(Service)