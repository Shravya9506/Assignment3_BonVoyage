from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ('name', 'destination', 'description', 'destination_image')

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('vacation', 'name', 'source', 'trip_description', 'mode_of_transport', 'start_date', 'end_date', 'price', 'additional_benefits')
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }