from django.urls import path
from . import views

urlpatterns = [
    path('masters/', views.master_list, name='master_list'),
    path('services/', views.service_list, name='service_list'),
]