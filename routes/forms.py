from django import forms
from .models import Airport

# form for adding or editing an airport route.
class AirportRouteForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'parent', 'position', 'duration']

#form for the "Nth Node" search functionality.
class SearchNthNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(
        queryset=Airport.objects.all(),
        label="Starting Airport"
    )
    n_level = forms.IntegerField(min_value=1, label="Nth Level")
    position = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')], label="Position")