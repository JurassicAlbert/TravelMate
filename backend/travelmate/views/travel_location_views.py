from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models.travel_location import TravelLocation
from ..models.travel_history import TravelHistory
from ..models.user_preferences import UserPreferences
from ..forms.travel_location_form import TravelLocationForm
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from decouple import config
import openai

class TravelLocationView:
    @login_required
    def location_list(request):
        locations = TravelLocation.objects.all()
        return render(request, 'travel_locations.html', {'locations': locations})

    @login_required
    def add_location(request):
        if request.method == 'POST':
            form = TravelLocationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('location_list')
        else:
            form = TravelLocationForm()
        return render(request, 'add_travel_location.html', {'form': form})

class TravelContext:
    @staticmethod
    def get_top_recommendations(user, num_recommendations=5):
        try:
            user_preferences = UserPreferences.objects.get(user=user)
        except UserPreferences.DoesNotExist:
            return []

        all_locations = TravelLocation.objects.all()
        user_vector = np.array([
            1 if user_preferences.prefers_category == location.category else 0
            for location in all_locations
        ])

        location_vectors = np.array([
            [location.recommended_by.count()] for location in all_locations
        ])

        user_similarity = cosine_similarity([user_vector], location_vectors).flatten()

        preference_weight = 0.7
        recommendation_weight = 0.3
        weighted_scores = (
            preference_weight * user_similarity +
            recommendation_weight * (location_vectors.flatten() / location_vectors.max())
        )

        top_indices = weighted_scores.argsort()[-num_recommendations:][::-1]
        top_locations = [all_locations[index] for index in top_indices]

        return [
            f"{location.name}: {location.description} (Category: {location.category})"
            for location in top_locations
        ]

class PersonalizedTravelRecommendation:
    @login_required
    def recommend(request):
        openai.api_key = config("OPENAI_API_KEY")
        user = request.user
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
                return render(request, 'recommendations.html', {'recommendations': recommendations})
        else:
            form = TravelLocationForm()
        return render(request, 'add_travel_location.html', {'form': form})