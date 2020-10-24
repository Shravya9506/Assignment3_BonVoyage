from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ObjectDoesNotExist

from .models import Customer, User, CustomerFavoriteVacation


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')

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

    def phone(self, instance):
        try:
            return instance.user.phone
        except ObjectDoesNotExist:
            return 'ERROR!!'

class CustomerFavoritesList(admin.ModelAdmin):
    list_display = ('id', 'customer_username', 'trip_name')

    def customer_username(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.customer.user.username
        except ObjectDoesNotExist:
            return 'ERROR!!'

    def trip_name(self, instance):  # name of the method should be same as the field given in `list_display`
        try:
            return instance.trip.name
        except ObjectDoesNotExist:
            return 'ERROR!!'


admin.site.register(CustomerFavoriteVacation, CustomerFavoritesList)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(User, UserAdmin)
