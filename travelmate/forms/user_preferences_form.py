from django import forms
from travelmate.models.user_preferences import UserPreferences

class UserPreferencesForm(forms.ModelForm):
    """
    Form for managing user travel preferences.
    """
    CATEGORY_CHOICES = [
        ('attraction', 'Attraction'),
        ('restaurant', 'Restaurant'),
        ('hotel', 'Hotel'),
        ('park', 'Park'),
        ('museum', 'Museum'),
        ('beach', 'Beach'),
        ('shopping', 'Shopping Center'),
        ('historical', 'Historical Site'),
        ('nightlife', 'Nightlife Spot'),
        ('nature', 'Natural Reserve'),
        ('adventure', 'Adventure Activity'),
        ('cultural', 'Cultural Experience'),
    ]

    prefers_category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Preferred Travel Category"
    )

    class Meta:
        model = UserPreferences
        fields = ['prefers_category']

    def clean_prefers_category(self):
        """
        Validate selected category against predefined options.
        """
        prefers_category = self.cleaned_data.get('prefers_category')
        if prefers_category not in dict(self.CATEGORY_CHOICES).keys():
            raise forms.ValidationError("Invalid category selected.")
        return prefers_category
