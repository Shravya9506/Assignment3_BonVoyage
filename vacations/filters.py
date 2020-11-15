from django import forms
from django_filters import CharFilter, RangeFilter, ModelMultipleChoiceFilter, FilterSet
from django_filters.widgets import RangeWidget, DateRangeWidget

from .models import Vacation, Trip
from django.utils.translation import ugettext_lazy as _

class VacationFilter(FilterSet):
    # destination = django_filters.MultipleChoiceFilter(choices=[(c.pk,c.destination) for c in Vacation.objects.all()],
    #                                                   widget=forms.CheckboxSelectMultiple)
    destination = ModelMultipleChoiceFilter(queryset=Vacation.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple,
                                                    label="Destination")
    class Meta:
        model = Vacation
        fields = ['destination']



class TripFilter(FilterSet):
    name = ModelMultipleChoiceFilter(queryset=Trip.objects.all(),
                                                           widget=forms.CheckboxSelectMultiple,
                                                           label="Trip Name")
    source = CharFilter(field_name='source', lookup_expr='icontains', label='Starting from (City)')
    class Meta:
        model = Trip
        fields = {'name'}
