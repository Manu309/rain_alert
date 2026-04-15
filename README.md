# Rain Alert

A Python application that checks weather forecasts and sends WhatsApp alerts when rain is expected.

## Features

- Fetches weather data from OpenWeatherMap API
- Sends WhatsApp notifications via Twilio
- Checks 4-hour forecast for rain conditions

## Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:
   ```
   OWM_API_KEY=your_openweathermap_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   ```

3. Update the latitude and longitude in `main.py` for your location

4. Run the application:
   ```bash
   python main.py
   ```

## GitHub Actions Setup

1. Add secrets to your GitHub repository:
   - Go to **Settings** → **Secrets and variables** → **Actions**
   - Add three repository secrets:
     - `OWM_API_KEY`
     - `TWILIO_ACCOUNT_SID`
     - `TWILIO_AUTH_TOKEN`

2. The workflow will automatically run every 3 hours (or manually trigger via Actions tab)

## Requirements

- Python 3.x
- requests
- twilio

## APIs Used

- [OpenWeatherMap](https://openweathermap.org/) - Weather data
- [Twilio](https://www.twilio.com/) - WhatsApp messaging

