FastAPI User Management Microservice
Overview
This project is a FastAPI-based microservice designed to manage user profiles with full CRUD (Create, Read, Update, Delete) functionality. It integrates with an external weather API, handles user states, implements concurrency with multi-threading, and secures endpoints using JWT authentication.

Features
User Management: Perform CRUD operations on user profiles.
Weather Integration: Fetch weather information based on the user's city.
State Management: Manage and update user states (e.g., Active, Inactive, Suspended).
Concurrency: Use threading for background tasks.
JWT Authentication: Secure endpoints using JSON Web Tokens.
MongoDB Integration: Use MongoDB for data storage.
Technologies Used
FastAPI: Web framework for building APIs.
MongoDB: NoSQL database for data storage.
pymongo: Python driver for MongoDB.
JWT: JSON Web Tokens for authentication.
Uvicorn: ASGI server for serving the FastAPI application.
Threading: For executing background tasks concurrently.
OpenWeatherMap API: External API for fetching weather data.


Project Structure


project/
│
├── auth/
│   └── jwt_bearer.py             # JWT Bearer token authentication class
├── config/
│   └── db.py                     # MongoDB configuration and connection setup
├── models/
│   ├── admin.py                  # Pydantic model for Admin users
│   ├── authuser.py               # Pydantic model for Authenticated users
│   ├── state.py                  # Pydantic model for user state
│   └── user.py                   # Pydantic model for basic user profile
├── routes/
│   ├── admin.py                  # Routes for Admin users
│   ├── authuser.py               # Routes for Authenticated users
│   ├── batch_processing.py       # Batch processing routes
│   ├── state.py                  # Routes for managing user states
│   └── user.py                   # Routes for basic user operations
├── schemas/
│   └── user.py                   # Schemas for converting MongoDB documents to Python dictionaries
├── tasks/
│   └── scheduler.py              # Scheduler for automatic tasks like user state updates
├── main.py                       # Main entry point for the FastAPI application
├── requirements.txt              # Python dependencies
└── weatherApi.py                 # Integration with the OpenWeatherMap API

Installation

Prerequisites
Python 3.8+
MongoDB instance (local or cloud-based, e.g., MongoDB Atlas)
Step-by-Step Setup
Clone the repository:


git clone https://github.com/NweOne-sd/WeatherApi/tree/finall

cd fastapi-user-management
Create a virtual environment:



python -m venv env
Activate the virtual environment:


source env/Scripts/activate
Windows CMD:


.\env\Scripts\activate
PowerShell:
bash
Copy code
.\env\Scripts\Activate
Install the dependencies:


Copy code
pip install -r requirements.txt
Set up MongoDB:

Update the MongoDB URI in config/db.py:
python
Copy code
mongo_uri = "your_mongodb_uri"
Set up the Weather API:

Update the API key in weatherApi.py:
python

api_key = "your_openweathermap_api_key"
Run the application:


uvicorn main:app --reload
Access the API documentation:

Open your browser and go to http://127.0.0.1:8000/docs to access the automatically generated Swagger UI.