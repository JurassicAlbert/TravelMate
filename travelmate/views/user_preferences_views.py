from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.user_preferences_form import UserPreferencesForm
from ..models.user_preferences import UserPreferences

class UserPreferencesView:
    @login_required
    def preferences(request):
        preferences, created = UserPreferences.objects.get_or_create(user=request.user)
        if request.method == 'POST':
            form = UserPreferencesForm(request.POST, instance=preferences)
            if form.is_valid():
                form.save()
                return redirect('preferences')
        else:
            form = UserPreferencesForm(instance=preferences)
        return render(request, 'preferences.html', {'form': form})