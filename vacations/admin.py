from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from .models import Vacation, Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('source', 'price', 'vacation_name', 'destination')
    list_filter = ('source', 'price', 'start_date')
    exclude = ("slug",)

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

class VacationAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination')
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