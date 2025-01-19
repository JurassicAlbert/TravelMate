from django.shortcuts import render, redirect
from django.contrib.auth import login
from ..models.app_user import AppUser
from ..models.travel_location import TravelLocation
from ..models.user_preferences import UserPreferences
from ..forms.travel_location_form import TravelLocationForm
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

        all_locations = TravelLocation.objects.all()

        # Poprawka: upewnienie się, że macierz ma odpowiedni wymiar
        user_vector = np.array([
            1 if user_preferences.prefers_category == location.category else 0
            for location in all_locations
        ]).reshape(1, -1)

        location_vectors = np.array([
            [1 if user_preferences.prefers_category == location.category else 0 for location in all_locations]
        ])

        # Debugowanie wymiarów
        print(f"user_vector shape: {user_vector.shape}")
        print(f"location_vectors shape: {location_vectors.shape}")

        # Obliczanie podobieństwa kosinusowego
        user_similarity = cosine_similarity(user_vector, location_vectors).flatten()

        preference_weight = 0.7
        recommendation_weight = 0.3
        weighted_scores = (
            preference_weight * user_similarity +
            recommendation_weight * (location_vectors.sum(axis=0) / location_vectors.sum())
        )

        top_indices = weighted_scores.argsort()[-num_recommendations:][::-1]
        top_locations = [all_locations[int(index)] for index in top_indices]  # Konwersja na int

        return [
            f"{location.name}: {location.description} (Category: {location.category})"
            for location in top_locations
        ]

class PersonalizedTravelRecommendation:
    def recommend(request):
        user = auto_login_user(request)
        openai.api_key = config("OPENAI_API_KEY")
        top_recommendations = TravelContext.get_top_recommendations(user=user)
        assistant_context = "\n".join(top_recommendations)

        if request.method == 'POST':
            form = TravelLocationForm(request.POST)
            if form.is_valid():
                form.save()
                user_query = form.cleaned_data.get('name')

                messages = [
                    {"role": "system", "content": "You are a travel assistant providing recommendations."},
                    {"role": "user", "content": f"Based on my preferences, where should I go next? {user_query}"},
                    {"role": "assistant", "content": assistant_context},
                ]
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4o-mini",
                        messages=messages,
                        temperature=1
                    )
                    recommendations = response['choices'][0]['message']['content']
                except Exception as e:
                    recommendations = f"Error fetching recommendations: {str(e)}"

                return render(request, 'recommendations.html', {'recommendations': recommendations, 'user': user})
        else:
            form = TravelLocationForm()

        return render(request, 'add_travel_location.html', {
            'form': form,
            'recommendations': None,
            'user': user
        })
