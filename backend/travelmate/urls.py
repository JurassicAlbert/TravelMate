from django.urls import path
from .views.app_user_views import UserView
from .views.review_views import ReviewView
from .views.travel_history_views import TravelHistoryView
from .views.travel_location_views import TravelLocationView, PersonalizedTravelRecommendation
from .views.user_preferences_views import UserPreferencesView

urlpatterns = [
    # Ścieżki dla użytkownika
    path('register/', UserView.register, name='register'),
    path('login/', UserView.user_login, name='login'),
    path('logout/', UserView.user_logout, name='logout'),
    path('password-reset/', UserView.password_reset, name='password_reset'),

    # Ścieżki dla recenzji
    path('reviews/', ReviewView.review_list, name='review_list'),
    path('reviews/add/', ReviewView.add_review, name='add_review'),
    path('reviews/edit/<int:review_id>/', ReviewView.edit_review, name='edit_review'),

    # Ścieżki dla historii podróży
    path('travel-history/', TravelHistoryView.history_list, name='history_list'),
    path('travel-history/add/', TravelHistoryView.add_history, name='add_history'),
    path('travel-history/delete/<int:history_id>/', TravelHistoryView.delete_history, name='delete_history'),

    # Ścieżki dla lokalizacji podróży
    path('travel-locations/', TravelLocationView.location_list, name='location_list'),
    path('travel-locations/add/', TravelLocationView.add_location, name='add_location'),
    path('travel-recommendations/', PersonalizedTravelRecommendation.recommend, name='recommend'),

    # Ścieżki dla preferencji użytkownika
    path('preferences/', UserPreferencesView.preferences, name='preferences'),
]
