import os
from dotenv import load_dotenv

# Take environment variables from .env.
load_dotenv(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
)

DEBUG = os.getenv("ENVIRONMENT") == "DEVELOPMENT"

APP_ROOT = os.getenv("APP_ROOT", "")
PORT = os.getenv("PORT", 8536)

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Google bucket configs
G_BUCKET_NAME = os.getenv("G_BUCKET_NAME")

WORKOUT_PASS = os.getenv("EDIT_WORKOUT_PASS", None)
