from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import csv
from .models import Customer, User, CustomerFavoriteVacation

class CustomerExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['User Id', 'Customer Name', 'Username', 'Email', 'Phone', 'Marital status']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=Customers_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for customer in queryset:
            writer.writerow([customer.user.id, customer.user.first_name + " " + customer.user.last_name,
                             customer.user.username, customer.user.email, customer.user.phone, \
                             "Married" if customer.marital_status == "MA" else "Unmarried" if customer.marital_status == "UM" else ""])

        return response

    export_as_csv.short_description = "Export Selected as CSV"

class CustomerFavoriteVacationExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['Id', 'Customer Name', 'Vacation destination']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=CustomerFavoriteVacation_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for customerFavoriteVacation in queryset:
            writer.writerow([customerFavoriteVacation.id,
                             customerFavoriteVacation.customer.user.first_name + " " + customerFavoriteVacation.customer.user.last_name,
                             customerFavoriteVacation.vacation.destination])

        return response

    export_as_csv.short_description = "Export Selected as CSV"


class UserExportCsvMixin:
    def export_as_csv(self, request, queryset):
        # Specify the header field names
        field_names = ['User Id', 'Name', 'Username', 'Email', 'Is admin', 'Is customer']
        response = HttpResponse(content_type='text/csv')
        # Specify the filename
        response['Content-Disposition'] = 'attachment; filename=Users_report.csv'
        writer = csv.writer(response)
        writer.writerow(field_names)
        for user in queryset:
            writer.writerow([user.id, user.first_name + " " + user.last_name,
                             user.username, user.email, "True" if user.is_superuser else "False",
                             "True" if user.is_customer else "False"])

        return response

    export_as_csv.short_description = "Export Selected as CSV"


class UserAdmin(admin.ModelAdmin, UserExportCsvMixin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    actions = ["export_as_csv"]

class CustomerAdmin(admin.ModelAdmin, CustomerExportCsvMixin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    actions = ["export_as_csv"]

    def username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.user.username
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def first_name(self, instance):
        try:
            return instance.user.first_name
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def last_name(self, instance):
        try:
            return instance.user.last_name
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def email(self, instance):
        try:
            return instance.user.email
        except ObjectDoesNotExist:
            return 'ERROR!!'


class CustomerFavoritesList(admin.ModelAdmin, CustomerFavoriteVacationExportCsvMixin):
    list_display = ('id', 'customer_username', 'vacation_destination')
    actions = ["export_as_csv"]

    def customer_username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.customer.user.username
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def vacation_destination(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.vacation.destination
        except ObjectDoesNotExist:
            return 'ERROR!!'


admin.site.register(CustomerFavoriteVacation, CustomerFavoritesList)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
