from django import forms
from travelmate.models.travel_location import TravelLocation


class TravelLocationForm(forms.ModelForm):
    """
    Form for adding and managing travel locations.
    """

    class Meta:
        model = TravelLocation
        fields = ['name', 'description', 'category', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
        }

    def clean_latitude(self):
        """
        Validate that latitude is within valid range.
        """
        latitude = self.cleaned_data.get('latitude')
        if latitude < -90 or latitude > 90:
            raise forms.ValidationError("Latitude must be between -90 and 90 degrees.")
        return latitude

    def clean_longitude(self):
        """
        Validate that longitude is within valid range.
        """
        longitude = self.cleaned_data.get('longitude')
        if longitude < -180 or longitude > 180:
            raise forms.ValidationError("Longitude must be between -180 and 180 degrees.")
        return longitude

from django import forms

class TravelQueryForm(forms.Form):
    """
    Form for querying travel recommendations.
    """
    query = forms.CharField(
        label="Gdzie chcesz podróżować?",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wpisz miejsce podróży'})
    )
