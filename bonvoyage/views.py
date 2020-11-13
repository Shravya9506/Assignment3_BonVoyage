from django.shortcuts import redirect, render
from vacations.models import Vacation, Trip
from .models import *

def home(request):
    vacations = Vacation.objects.all()
    return render(request, 'home.html', {'vacations': vacations})

def message(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name', '')
        lastname = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(firstname,lastname, email, phone,message)
        Message.objects.create(sender_name = firstname + " " + lastname, email = email, phone = phone, message = message)
        return render(request, 'contact_us_done.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')
