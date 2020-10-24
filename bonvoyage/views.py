from django.shortcuts import redirect, render
from vacations.models import Vacation, Trip


def home(request):
    vacations = Vacation.objects.all()
    trips = Trip.objects.all()
    # context = {'vacations': vacations,
    #            'trips' : trips}
    return render(request, 'home.html', {'vacations': vacations})

