import os

DEBUG = os.getenv("ENVIRONMENT") == "DEVELOPMENT"

APP_ROOT = os.getenv("APP_ROOT", "")
PORT = os.getenv("PORT", 8536)

GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Google bucket configs
G_BUCKET_NAME = os.getenv("G_BUCKET_NAME")