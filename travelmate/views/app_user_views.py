from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from ..forms.password_reset_form import PasswordResetForm
from ..models.app_user import AppUser
from ..forms.user_registration_form import UserRegistrationForm
from ..forms.user_login_form import UserLoginForm


class UserView:
    @staticmethod
    def register(request):
        """
        Handles user registration with plain text password storage.
        """
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = AppUser.objects.create(
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password']  # Storing password in plain text
                )
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    @staticmethod
    def user_login(request):
        """
        Handles user login by checking plain text password.
        """
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = AppUser.objects.get(email=email)
                    if user.password == password:  # Directly compare plain text password
                        login(request, user)
                        next_url = request.GET.get('next', 'recommend')
                        return redirect(next_url)
                    else:
                        form.add_error(None, 'Invalid email or password')
                except AppUser.DoesNotExist:
                    form.add_error(None, 'Invalid email or password')
        else:
            form = UserLoginForm()
        return render(request, 'index.html', {'form': form})

    @staticmethod
    def user_logout(request):
        """
        Handles user logout.
        """
        logout(request)
        return redirect('login')

    @staticmethod
    def password_reset(request):
        """
        Handles password reset by sending an email with a reset link.
        """
        if request.method == 'POST':
            form = PasswordResetForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                try:
                    user = AppUser.objects.get(email=email)
                    token = default_token_generator.make_token(user)
                    reset_link = request.build_absolute_uri(f"/reset-password/{user.pk}/{token}/")
                    send_mail(
                        'Password Reset Request',
                        f'Click the link to reset your password: {reset_link}',
                        'noreply@example.com',
                        [email],
                    )
                    return redirect('password_reset_done')
                except AppUser.DoesNotExist:
                    form.add_error(None, 'No account found with this email.')
        else:
            form = PasswordResetForm()
        return render(request, 'password_reset.html', {'form': form})
