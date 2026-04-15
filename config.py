import os
from dotenv import load_dotenv

# Load from .env file if it exists (for local development)
load_dotenv()

# Read from environment variables (set by GitHub Actions or .env file locally)
OWM_API_KEY = os.getenv("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Validate credentials are loaded
if not all([OWM_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN]):
    raise ValueError("Missing required environment variables. Check GitHub Secrets or .env file configuration.")

