# TravelMate: Your Personal Travel Assistant

## What are we creating?

TravelMate is an innovative travel assistant application designed to enhance your travel planning experience. It allows users to create personalized travel plans, discover must-visit attractions, restaurants, and hotels, and get answers to location-based queries. Unlike a simple interface for ChatGPT, TravelMate remembers user preferences, favorite places, and past decisions to offer curated recommendations tailored to their unique travel style. Additionally, the app suggests one bonus destination recommended by fellow travelers who have visited the area.

---

## Why are we creating this?

Travel planning can be time-consuming and overwhelming with the abundance of available options. TravelMate aims to simplify this process by:

- **Personalization**: Offering recommendations based on user preferences and past trips.
- **Efficiency**: Consolidating information in one place for seamless travel planning.
- **Community**: Including peer-recommended locations to make the experience unique and trusted.
- **Innovation**: Leveraging AI and data storage to create a dynamic, user-centric travel tool that evolves with the user’s preferences.

---

## How are we creating this?

TravelMate is built with cutting-edge technologies, combining robust backend logic, a responsive frontend interface, and intelligent AI integrations:

1. **Frontend**: Developed in Vue.js, it ensures an intuitive and user-friendly interface.
2. **Backend**: Built using Django, the backend manages user authentication, data storage, and connections to external APIs.
3. **Data Integration**:
   - **GPT API**: Generates dynamic content and provides location-based recommendations.
   - **Google Maps API**: Offers map visualization and detailed location data.
4. **User-centric Data Storage**: A database in sqlite captures user preferences, favorite spots, and travel history to enable personalized recommendations.

---

## Installation Guide

Follow these steps to set up the TravelMate project on your local machine.

### Prerequisites

Ensure you have the following installed:
- Python 3.12.7 and Django
- Node.js and npm
- A virtual environment tool (e.g., `venv`)
- Access to GPT API keys

---

### Backend Setup (Django)

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/travelmate.git
cd travelmate/backend

# 2. Create a Virtual Environment
python -m venv env
source env/bin/activate   # On Windows: `env\Scripts\activate`

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Set Environment Variables
# Create a `.env` file in the `backend` directory and add:
# GPT_API_KEY=your_gpt_api_key
# GOOGLE_MAPS_API_KEY=your_google_maps_api_key

# 5. Migrate Database
python manage.py makemigrations
python manage.py migrate

# 6. Run the Server
python manage.py runserver
```

# Frontend Setup (Vue.js)
## 1. Navigate to the Frontend Directory
cd travelmate/frontend

## 2. Install Dependencies
npm install

## 3. Configure API Endpoints
## Update the `API_URL` in the frontend `.env` file to point to the backend server:
## VITE_API_URL=http://127.0.0.1:8000/api/

## 4. Run the Frontend Server
npm run dev

# Accessing the application

## 1. Open your browser and visit the frontend development server (default):
- http://localhost:5173

## 2. Sign up or log in to start planning your personalized travel experiences.

## Features to Explore

- **Customized Trip Plans**: Get itineraries tailored to your preferences.
- **Community-Driven Recommendations**: Discover hidden gems loved by other travelers.
- **Multilingual Support**: Plan your travels effortlessly, regardless of the language barrier.
- **Seamless User Experience**: Enjoy a fluid interface and cohesive functionality.

Happy traveling with **TravelMate**! 🌍✈️
