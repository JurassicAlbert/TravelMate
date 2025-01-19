# Changelog for TravelMate

## Version 1.0.0

### General
- Initialized the project with a clear separation of backend and frontend.
- Added `.gitignore` files to exclude unnecessary files from version control.
- Created `Readme.md` to provide an overview of the project, setup instructions, and usage guidelines.

### Backend
- **Core Configuration:**
  - Added `manage.py` for Django project management.
  - Configured `settings.py`, including database and app settings.
  - Defined URL routing in `urls.py`.
  - Included ASGI (`asgi.py`) and WSGI (`wsgi.py`) for server communication.
  - Implemented modular settings to allow easier scalability and environment-specific configurations.

- **Models:**
  - Created `app_user.py` for handling user data, including authentication and profile management.
  - Added `review.py` for storing user reviews of places with ratings and optional comments.
  - Implemented `travel_history.py` to track user travel history, including timestamps and location metadata.
  - Designed `travel_location.py` for storing information about travel locations, such as geocoordinates and descriptions.
  - Built `user_preferences.py` to store user-specific preferences, including notification settings and favorite categories.

- **Serializers:**
  - Added serializers for all models to handle JSON data: `app_user_serializer.py`, `review_serializer.py`, `travel_history_serializer.py`, `travel_location_serializer.py`, `user_preferences_serializer.py`.
  - Ensured validation logic is embedded in serializers to enforce data integrity.

- **Views:**
  - Developed RESTful API endpoints in: `app_user_views.py`, `review_views.py`, `travel_history_views.py`, `travel_location_views.py`, `user_preferences_views.py`.
  - Included pagination and filtering options in API endpoints for better usability.

- **Fixtures and Migrations:**
  - Provided initial data with `fixtures.json`, including sample users and travel locations.
  - Set up Django migrations for database schema updates.

### Frontend
- **Core Configuration:**
  - Configured project settings in `package.json`, `package-lock.json`, `babel.config.js`, and `vue.config.js`.
  - Integrated ESLint for code linting and formatting consistency.

- **Public Assets:**
  - Added `favicon.ico` as the application icon.
  - Set up `index.html` as the entry point for the application.
  - Included meta tags for SEO and social media sharing.

- **Source Code:**
  - Created `App.vue` as the root component, including a global navigation bar.
  - Built reusable components:
    - `HelloWorld` (example component).
    - `PlaceCard.vue` for displaying travel place cards with image, name, and summary.
  - Developed main views:
    - `HomePage.vue` for the home page, featuring popular locations.
    - `PlaceDetails.vue` for detailed place information, including user reviews.
    - `SearchPlaces.vue` for searching travel locations with filters.
    - `UserPreferences.vue` for managing user settings and preferences.
    - `VisitedPlaces.vue` for displaying visited places with timestamps.
  - Configured router in `src/router/index.js` for handling application navigation, including route guards.

- **Assets:**
  - Added `logo.png` for branding.
  - Structured asset folders for better organization of images and styles.

## Summary
This version establishes the foundational structure for both the backend (Django) and frontend (Vue.js). It includes models, serializers, views, and essential configurations for backend functionality. The frontend provides a user-friendly interface with navigation, dynamic views, and responsive design to enhance user experience.

