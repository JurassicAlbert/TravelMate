from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views.app_user_views import UserRegistrationView, UserLoginView, PasswordResetView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views.travel_location_views import TravelLocationViewSet, PersonalizedTravelRecommendationView
from .views.travel_history_views import TravelHistoryViewSet
from .views.user_preferences_views import UserPreferencesViewSet

router = DefaultRouter()
router.register(r'travel-locations', TravelLocationViewSet)
router.register(r'travel-history', TravelHistoryViewSet)
router.register(r'user-preferences', UserPreferencesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('travel-recommendations/', PersonalizedTravelRecommendationView.as_view(), name='travel_recommendations'),
    path('', include(router.urls)),
]

# Serve review_photos files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
