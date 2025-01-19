from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..models.app_user import AppUser
from ..models.travel_location import TravelLocation
from ..models.user_preferences import UserPreferences
from ..forms.travel_location_form import TravelLocationForm
from ..forms.travel_location_form import TravelQueryForm
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from decouple import config
import openai

# Funkcja automatycznego logowania użytkownika "Jan Kowalski"
def auto_login_user(request):
    user, created = AppUser.objects.get_or_create(
        email="jan.kowalski@example.com",
        defaults={
            "first_name": "Jan",
            "last_name": "Kowalski",
            "password": "haslo123",
            "is_active": True,
            "is_staff": False
        }
    )
    if not request.user.is_authenticated:
        login(request, user)
    return user

class TravelLocationView:
    def location_list(request):
        user = auto_login_user(request)  # Logowanie domyślnego użytkownika
        locations = TravelLocation.objects.all()
        return render(request, 'travel_locations.html', {'locations': locations, 'user': user})

    def add_location(request):
        user = auto_login_user(request)
        if request.method == 'POST':
            form = TravelLocationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('location_list')
        else:
            form = TravelLocationForm()
        return render(request, 'add_travel_location.html', {'form': form, 'user': user})

class TravelContext:
    @staticmethod
    def get_top_recommendations(user, num_recommendations=5):
        try:
            user_preferences = UserPreferences.objects.get(user=user)
        except UserPreferences.DoesNotExist:
            return []

        all_locations = list(TravelLocation.objects.all())

        user_vector = np.array([
            1 if user_preferences.prefers_category == location.category else 0
            for location in all_locations
        ]).reshape(1, -1)

        location_vectors = np.array([
            [1 if user_preferences.prefers_category == location.category else 0 for location in all_locations]
        ])

        # Obliczanie podobieństwa kosinusowego
        user_similarity = cosine_similarity(user_vector, location_vectors).flatten()

        preference_weight = 0.7
        recommendation_weight = 0.3
        weighted_scores = (
            preference_weight * user_similarity +
            recommendation_weight * (location_vectors.sum(axis=0) / location_vectors.sum())
        )

        top_indices = weighted_scores.argsort()[-num_recommendations:][::-1]
        top_locations = [all_locations[int(index)] for index in top_indices]

        return [
            f"{location.name}: {location.description} (Category: {location.category})"
            for location in top_locations
        ]

class PersonalizedTravelRecommendation:
    def recommend(request):
        user = auto_login_user(request)
        openai.api_key = config("OPENAI_API_KEY")

        recommendations = None
        if request.method == 'POST':
            form = TravelQueryForm(request.POST)
            if form.is_valid():
                user_query = form.cleaned_data.get('query')


                messages = [
                    {"role": "system", "content": "Jesteś asystentem podróży, który udziela rekomendacji."},
                    {"role": "user", "content": f"Gdzie mogę podróżować? {user_query}"},
                ]

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        temperature=1
                    )
                    recommendations = response['choices'][0]['message']['content']
                except Exception as e:
                    recommendations = f"Błąd podczas pobierania rekomendacji: {str(e)}"
        else:
            form = TravelQueryForm()

        return render(request, 'travel_recommendations.html', {
            'form': form,
            'recommendations': recommendations,
            'user': user
        })
