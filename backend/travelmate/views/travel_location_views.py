import openai
import numpy as np
from decouple import config
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ..serializers import TravelLocationSerializer
from ..models import UserPreferences, TravelHistory, TravelLocation


class TravelLocationViewSet(ModelViewSet):
    """
    ViewSet for performing CRUD operations on TravelLocation.
    """
    queryset = TravelLocation.objects.all()
    serializer_class = TravelLocationSerializer


class TravelContext:
    @staticmethod
    def get_top_recommendations(user, num_recommendations=5):
        """
        Get the top recommendations based on cosine similarity.

        Parameters:
            user (AppUser): The user for whom recommendations are being generated.
            num_recommendations (int): Number of recommendations to return.

        Returns:
            List[str]: Descriptions of the top recommended travel locations.
        """
        # Step 1: Fetch user preferences and travel history
        try:
            user_preferences = UserPreferences.objects.get(user=user)
        except UserPreferences.DoesNotExist:
            return []

        # Step 2: Get all travel locations from the database
        all_locations = TravelLocation.objects.all()

        # Step 3: Represent user preferences and travel locations as vectors
        # User preference vector
        user_vector = np.array([
            1 if user_preferences.prefers_category == location.category else 0
            for location in all_locations
        ])

        # Location vectors (recommended weight by other users)
        location_vectors = []
        for location in all_locations:
            # Calculate how many users have recommended this location
            recommendation_score = location.recommended_by.count()
            location_vectors.append(np.array([recommendation_score]))

        location_vectors = np.array(location_vectors)

        # Step 4: Compute cosine similarity between user preferences and locations
        user_similarity = cosine_similarity([user_vector], location_vectors).flatten()

        # Step 5: Add weighted scoring
        # Higher weight for user preferences
        preference_weight = 0.7
        # Lower weight for popularity
        recommendation_weight = 0.3

        weighted_scores = (
                preference_weight * user_similarity +
                recommendation_weight * (location_vectors.flatten() / location_vectors.max())
        )

        # Step 6: Get the top N recommendations
        top_indices = weighted_scores.argsort()[-num_recommendations:][::-1]
        top_locations = [all_locations[index] for index in top_indices]

        # Return descriptions of top locations
        return [
            f"{location.name}: {location.description} (Category: {location.category})"
            for location in top_locations
        ]


class PersonalizedTravelRecommendationView(APIView):
    """
    API View for generating personalized travel recommendations using OpenAI.
    """
    permission_classes = [IsAuthenticated]

    # System prompt and default user prompt as class properties
    system_prompt = (
        "You are a highly intelligent travel assistant. Use the user's preferences and context to suggest personalized "
        "travel destinations."
    )
    user_prompt = "Based on my preferences and travel history, where should I go next?"

    # Initialize OpenAI API key
    openai.api_key = config("OPENAI_API_KEY")
    client = OpenAI(api_key=config("OPENAI_API_KEY"))

    def post(self, request):
        """
        Handles POST requests to generate personalized travel recommendations.
        """
        user = request.user  # Get the currently logged-in user

        # Fetch the top recommendations for the current user
        top_recommendations = TravelContext.get_top_recommendations(user=user)

        # Prepare assistant context (recommendations as a single text block)
        assistant_context = "\n".join(top_recommendations)

        # Combine user query with the default user prompt
        user_query = request.data.get("query", "")
        user_prompt = f"{self.user_prompt}\n{user_query}"

        # Prepare messages for the OpenAI API
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt},
            {"role": "assistant", "content": assistant_context},
        ]

        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                messages=messages,
                model="gpt-4o-mini",
                temperature=1
            )
            recommendations = response['choices'][0]['message']['content']
        except Exception as e:
            return Response({"error": f"Failed to get recommendations: {str(e)}"}, status=500)

        return Response({"recommendations": recommendations}, status=200)
