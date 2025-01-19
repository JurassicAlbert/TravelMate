from django import forms

class PasswordResetForm(forms.Form):
    """
    Form for password reset.
    """
    email = forms.EmailField(label="Email")