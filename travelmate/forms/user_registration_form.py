from django import forms
from travelmate.models.app_user import AppUser


class UserRegistrationForm(forms.ModelForm):
    """
    Form for user registration.
    """
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ['email', 'first_name', 'last_name', 'password']
