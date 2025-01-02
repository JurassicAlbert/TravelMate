from django.contrib import admin
from .models.app_user import AppUser
from .models.travel_location import TravelLocation
from .models.travel_history import TravelHistory
from .models.user_preferences import UserPreferences


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    """
    Admin settings for the AppUser model.
    """
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'date_joined')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined',)


@admin.register(TravelLocation)
class TravelLocationAdmin(admin.ModelAdmin):
    """
    Admin settings for the TravelLocation model.
    """
    list_display = ('name', 'category', 'latitude', 'longitude')
    search_fields = ('name', 'category')
    list_filter = ('category',)
    ordering = ('name',)


@admin.register(TravelHistory)
class TravelHistoryAdmin(admin.ModelAdmin):
    """
    Admin settings for the TravelHistory model.
    """
    list_display = ('user', 'location', 'visited_at')
    search_fields = ('user__email', 'location__name')
    list_filter = ('visited_at',)
    ordering = ('-visited_at',)


@admin.register(UserPreferences)
class UserPreferencesAdmin(admin.ModelAdmin):
    """
    Admin settings for the UserPreferences model.
    """
    list_display = ('user', 'prefers_category')
    search_fields = ('user__email', 'prefers_category')
    list_filter = ('prefers_category',)
