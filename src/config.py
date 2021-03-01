import os

DEBUG = os.getenv("ENVIRONMENT") == "DEV"

APP_ROOT = os.getenv("APP_ROOT")
PORT = os.getenv("APP_PORT", 8536)

# Google bucket configs
G_BUCKET_URL = os.getenv("G_BUCKET_URL")
PATH = os.getenv("BUCKET_FILES_ROOT_PATH")