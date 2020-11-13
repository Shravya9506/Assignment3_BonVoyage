from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views



app_name = 'vacations'

urlpatterns = [
    path('vacations_list/', views.vacation_list, name='vacation_list'),
    path('vacations_list/<int:showFavorites>', views.vacation_list, name='favorites_vacation_list'),
    path('vacations_add/', views.add_vacation, name='add_vacation'),
    path('delete_vacation/<int:pk>', views.delete_vacation, name='delete_vacation'),
    path('edit_vacation/<int:pk>', views.edit_vacation, name='edit_vacation'),
    path('vacation_details/<int:pk>', views.vacation_details, name='vacation_details'),
    path('trip_details_pdf/<int:pk>', views.trip_details_pdf, name='trip_details_pdf'),
    path('trip_details/<int:pk>', views.trip_details, name='trip_details'),
    path('trip_add/', views.add_trip, name='add_trip'),
    path('delete_trip/<int:pk>', views.delete_trip, name='delete_trip'),
    path('edit_trip/<int:pk>', views.edit_trip, name='edit_trip'),
]