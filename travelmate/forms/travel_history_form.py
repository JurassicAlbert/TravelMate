from django import forms
from travelmate.models.travel_history import TravelHistory


class TravelHistoryForm(forms.ModelForm):
    """
    Form for adding and managing travel history records.
    """

    class Meta:
        model = TravelHistory
        fields = ['user', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
