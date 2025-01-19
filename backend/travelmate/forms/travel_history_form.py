from django import forms
from backend.travelmate.models.travel_history import TravelHistory


class TravelHistoryForm(forms.ModelForm):
    """
    Form for adding and managing travel history records.
    """
    visited_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label="Visited At"
    )

    class Meta:
        model = TravelHistory
        fields = ['location', 'visited_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].widget.attrs.update({'class': 'form-control'})
        self.fields['visited_at'].widget.attrs.update({'class': 'form-control'})
