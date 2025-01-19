from django import forms


class UserLoginForm(forms.Form):
    """
    Form for user login.
    """
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
