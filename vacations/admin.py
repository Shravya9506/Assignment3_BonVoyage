from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from .models import Vacation, Trip
from django.http import HttpResponse
import csv


class VacationExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['Vacation name', 'Destination', 'Description']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=Vacations_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for vacation in queryset:
            writer.writerow([vacation.name, vacation.destination, vacation.description])

        return response

    export_as_csv.short_description = "Export Selected as CSV"


class TripExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['Trip name', 'Starting point', 'Destination', 'Vacation name', 'Price', 'Start date', 'End date',\
                       'Trip description', 'Additional benefits']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=Trips_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for trip in queryset:
            writer.writerow([trip.name, trip.source, trip.vacation.destination, trip.vacation.name, trip.price,
                             trip.start_date.strftime("%A, %d %b %Y"), trip.end_date.strftime("%A, %d %b %Y"),
                             trip.trip_description, trip.additional_benefits])

        return response

    export_as_csv.short_description = "Export Selected as CSV"


class TripAdmin(admin.ModelAdmin, TripExportCsvMixin):
    list_display = ('source', 'price', 'vacation_name', 'destination')
    list_filter = ('source', 'price', 'start_date')
    exclude = ("slug",)
    actions = ["export_as_csv"]

    def vacation_name(self, instance):
        try:
            return instance.vacation.name
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def destination(self, instance):
        try:
            return instance.vacation.destination
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug']
        else:
            return []


class TripDetailsInline(admin.TabularInline):
    model = Trip
    exclude = ("slug",)


    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug']
        else:
            return []

class VacationAdmin(admin.ModelAdmin, VacationExportCsvMixin):
    list_display = ('name', 'destination')
    actions = ["export_as_csv"]
    inlines = [
        TripDetailsInline,
    ]
    exclude = ("slug",)
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['slug',]
        else:
            return []


admin.site.register(Vacation, VacationAdmin)
admin.site.register(Trip,TripAdmin)