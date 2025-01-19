from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator

from ..forms.password_reset_form import PasswordResetForm
from ..models.app_user import AppUserManager as AppUser
from ..forms.user_registration_form import UserRegistrationForm
from ..forms.user_login_form import UserLoginForm


class UserView:
    def register(request):
        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                user = AppUser(
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    password=form.cleaned_data['password']  # Store password as plain text
                )
                user.save()
                return redirect('login')
        else:
            form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def user_login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    user = AppUser.objects.get(email=email, password=password)
                    login(request, user)
                    return redirect('/')
                except AppUser.DoesNotExist:
                    form.add_error(None, 'Invalid email or password')
        else:
            form = UserLoginForm()
        return render(request, 'index.html', {'form': form})

    def user_logout(request):
        logout(request)
        return redirect('/')

    def password_reset(request):
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