from django.urls import path
from django.shortcuts import redirect
from .views.app_user_views import UserView
from .views.review_views import ReviewView
from .views.travel_history_views import TravelHistoryView
from .views.travel_location_views import TravelLocationView
from .views.user_preferences_views import UserPreferencesView
from .views.travel_location_views import PersonalizedTravelRecommendation

# Function to redirect to the travel recommendations page
def redirect_to_recommend(request):
    return redirect('recommend')

urlpatterns = [
    # Redirect to travel recommendations page by default
    path('', redirect_to_recommend, name='home'),

    # User paths
    path('register/', UserView.register, name='register'),
    path('login/', UserView.user_login, name='login'),
    path('logout/', UserView.user_logout, name='logout'),
    path('password-reset/', UserView.password_reset, name='password_reset'),

    # Review paths
    path('reviews/', ReviewView.review_list, name='review_list'),
    path('reviews/add/', ReviewView.add_review, name='add_review'),
    path('reviews/edit/<int:review_id>/', ReviewView.edit_review, name='edit_review'),

    # Travel history paths
    path('travel-history/', TravelHistoryView.history_list, name='history_list'),
    path('travel-history/add/', TravelHistoryView.add_history, name='add_history'),
    path('travel-history/delete/<int:history_id>/', TravelHistoryView.delete_history, name='delete_history'),

    # Travel recommendations path
    path('travel-recommendations/', PersonalizedTravelRecommendation.recommend, name='recommend'),

    # User preferences paths
    path('preferences/', UserPreferencesView.preferences, name='preferences'),
]
