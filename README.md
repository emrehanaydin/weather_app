# Weather App

## Introduction

This is a simple Django application that allows users to check the weather information for different locations. Users can add new locations and view the current weather data for those locations.

## Features

- **User Authentication:** Users can register, login, and logout. Only authenticated users can add new locations and view weather information.
- **Location Management:** Authenticated users can add new locations to the database.
- **Weather Information:** The application fetches weather information from an external API and displays it to the user.

## Installation

1. Clone this repository to your local machine:

git clone https://github.com/your_username/weather-app.git

2. Navigate to the project directory:

cd weather-app

3. Install dependencies:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Run the development server:

python manage.py runserver

6. Access the application at [http://localhost:8000](http://localhost:8000).

## Usage

1. Register a new account or log in with an existing one.
2. Add new locations from the dashboard.
3. View weather information for added locations on the dashboard.

## Technologies Used

- Django
- Django REST Framework
- PostgreSQL
- HTML
- CSS
- Java Script
