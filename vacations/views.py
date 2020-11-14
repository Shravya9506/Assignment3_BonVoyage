from django.shortcuts import redirect, render
from .models import *
import datetime
from django.db.models import Min, Max
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML, CSS
from django.shortcuts import get_object_or_404
from django.conf import settings
from .filters import *
from users.models import CustomerFavoriteVacation
from django.core.mail import EmailMessage
from io import BytesIO
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from users.models import Customer


def vacation_list(request, showFavorites = 0):
    trips = Trip.objects.filter(start_date__gte = datetime.datetime.today())
    trip_filter = TripFilter(request.GET, queryset=trips)
    trips = trip_filter.qs
    vacationsList = [trip.vacation.id for trip in trips]
    vacations = Vacation.objects.filter(pk__in = vacationsList)
    if showFavorites and not request.user.is_staff:
        favoriteVacations = [favorites.vacation.id for favorites in CustomerFavoriteVacation.objects.filter(customer__user_id= request.user.id)]
        vacations = Vacation.objects.filter(pk__in = favoriteVacations)
    vacation_filter = VacationFilter(request.GET, queryset=vacations)
    vacations = vacation_filter.qs
    return render(request, 'vacations_list.html', {'vacations': vacations, 'vacation_filter': vacation_filter, 'trip_filter' : trip_filter, 'favorites' :showFavorites})

def vacation_details(request, pk):
    vacation = Vacation.objects.filter(id=pk)
    active_trips = Trip.objects.filter(vacation = pk, start_date__gte = datetime.datetime.today())
    price_range = active_trips.all().aggregate(Min('price'), Max('price'))
    is_favorite = CustomerFavoriteVacation.objects.filter(customer = request.user.id, vacation=pk).exists()
    return render(request, 'vacation_details.html', {'vacation': vacation, 'trips': active_trips, 'price_range':price_range, 'is_favorite':is_favorite})

@staff_member_required
def add_vacation(request):
    if request.method == "POST":
        form = VacationForm(request.POST, request.FILES)
        if form.is_valid():
            vacation = form.save(commit=False)
            vacation.save()
            return redirect('vacations:vacation_details', pk=vacation.id)
    else:
        form = VacationForm()
    return render(request, 'add_vacation.html', {'form': form})

@staff_member_required
def delete_vacation(request, pk):
    vacation = get_object_or_404(Vacation, pk=pk)
    if request.method == "POST":
        vacation.delete()
        return redirect('vacations:vacation_list')
    return render(request, 'delete_vacation.html', {'vacation': vacation})

@staff_member_required
def edit_vacation(request, pk):
    vacation = get_object_or_404(Vacation, pk=pk)
    if request.method == "POST":
        form = VacationForm(request.POST, instance=vacation)
        if form.is_valid():
            vacation = form.save()
            vacation.save()
            return redirect('vacations:vacation_details', pk=vacation.id)
    else:
        form = VacationForm(instance=vacation)
    return render(request, 'edit_vacation.html', {'form': form, 'pk': pk})


def trip_details(request, pk):
    trip = get_object_or_404(Trip, id=pk)
    start_date = datetime.datetime.strptime(str(trip.start_date), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(str(trip.end_date), "%Y-%m-%d")
    diff = abs((end_date - start_date).days)
    return render(request, 'trip_details.html', { 'trip': trip, 'diff' : diff})

@staff_member_required
def delete_trip(request, pk):
    trip = get_object_or_404(Trip, id=pk)
    if request.method == "POST":
        trip.delete()
        return redirect('vacations:vacation_details',trip.vacation.id)
    return render(request, 'delete_trip.html', {'trip': trip})

@staff_member_required
def edit_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            trip = form.save()
            trip.save()
            return redirect('vacations:trip_details', pk=trip.id)
    else:
        form = TripForm(instance=trip)
    return render(request, 'edit_trip.html', {'form': form, 'pk': pk})

@staff_member_required
def add_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return redirect('vacations:trip_details', pk=trip.id)
    else:
        form = TripForm()
    return render(request, 'add_vacation.html', {'form': form})


@login_required
def trip_details_pdf(request, pk):
    trip = get_object_or_404(Trip, id=pk)
    start_date = datetime.datetime.strptime(str(trip.start_date), "%Y-%m-%d")
    end_date = datetime.datetime.strptime(str(trip.end_date), "%Y-%m-%d")
    diff = abs((end_date - start_date).days)
    # create invoice e-mail
    subject = 'Brochure of the trip - {}'.format(trip.name)
    message = 'Hello {},\n' \
              'Please find the attachment for the e-copy of the trip details you requested for. \n' \
              'Contact us in case you need assistance of any sort, our team is happy to assist you. \n' \
              'If you are interested in taking this trip, please contact us on the our details mentioned in the website. \n \n \n' \
              'Team Bonvoyage'.format(request.user.first_name+ " " + request.user.last_name)
    email = EmailMessage(subject,
                         message,
                         'admin@bonvoyage.com',
                         [request.user.email])

    html = render_to_string('trip_details_PDF.html',
                            { 'trip': trip, 'diff' : diff})
    out = BytesIO()
    HTML(string=html,base_url=request.build_absolute_uri()).write_pdf(out,
                                stylesheets=[CSS(settings.STATIC_ROOT + '/css/trip_details_pdf.css'), \
                                    CSS('https://use.fontawesome.com/releases/v5.7.0/css/all.css'),\
                                    CSS('https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css')])
    email.attach('Brochure of the {}.pdf'.format(trip.name),
                 out.getvalue(),
                 'application/pdf')
    #send e-mail
    email.send()
    return render(request, 'pdf_sent.html')