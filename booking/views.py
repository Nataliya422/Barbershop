# booking/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Master, Service, Review

def home(request):
    return render(request, 'home.html')

def master_list(request):
    masters = Master.objects.all()
    return render(request, 'master_list.html', {'masters': masters})

def add_review(request, master_id):
    master = get_object_or_404(Master, id=master_id)

    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        comment = request.POST.get('comment')
        rating = request.POST.get('rating')
        Review.objects.create(master=master, client_name=client_name, comment=comment, rating=rating)
        return redirect('master_list')

    return redirect('master_list')

def service_list(request):
    services = Service.objects.all()
    return render(request, 'service_list.html', {'services': services})

def about_us(request):
    return render(request, 'about_us.html')

def book_appointment(request):
    masters = Master.objects.all()
    services = Service.objects.all()

    print("All Masters:", masters)  # Отладочное сообщение для вывода всех мастеров
    print("All Services:", services)  # Отладочное сообщение для вывода всех услуг

    if request.method == 'POST':
        master_id = request.POST.get('master')
        service_id = request.POST.get('service')
        date = request.POST.get('date')
        time = request.POST.get('time')

        print("Selected Master ID:", master_id)  # Отладочное сообщение для вывода ID выбранного мастера
        print("Selected Service ID:", service_id)  # Отладочное сообщение для вывода ID выбранной услуги
        print("Selected Date:", date)  # Отладочное сообщение для вывода выбранной даты
        


        selected_master = get_object_or_404(Master, id=master_id)
        selected_service = get_object_or_404(Service, id=service_id)

    

        return render(request, 'book_appointment.html', {
            'masters': masters,
            'services': services,
            'selected_master': selected_master,
            'selected_service': selected_service,
            'date': date,
            'time': time
        })

    return render(request, 'book_appointment.html', {'masters': masters, 'services': services})

def reviews(request):
    reviews_list = Review.objects.all()
    return render(request, 'reviews.html', {'reviews': reviews_list})

def master_reviews(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    reviews = Review.objects.filter(master=master)
    return render(request, 'master_reviews.html', {'master': master, 'reviews': reviews})