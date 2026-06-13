Weather Alert

A Python weather alert application that fetches real-time weather data using the OpenWeatherMap API and detects rain conditions.

Features

- Fetches real-time weather information
- Detects rain conditions
- Displays weather details for a specified city
- Uses OpenWeatherMap API
- Secure API key management using ".env"

Technologies Used

- Python
- Requests
- Python-Dotenv
- OpenWeatherMap API
- GitHub Actions

Project Structure

weather-alert/

├── weather_alert.py

├── requirements.txt

├── .gitignore

├── .env (not tracked)

└── .github/

└── workflows/

    └── weather.yml

Installation

1. Clone the repository:

git clone https://github.com/Amritha1001-K/weather-alert.git
cd weather-alert

2. Install dependencies:

pip install -r requirements.txt

3. Create a ".env" file:

API_KEY=your_openweathermap_api_key

Usage

Run the application:

python weather_alert.py

The program will fetch weather data and notify the user if rain is detected.

GitHub Actions

This project includes a GitHub Actions workflow that automatically:

- Installs dependencies
- Runs the Python script
- Verifies the project builds successfully

Author

Amritha K