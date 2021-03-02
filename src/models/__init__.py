# Load firestore.
import config as c

import firebase_admin
from firebase_admin import credentials, firestore, storage
import google.cloud.storage

# Use the application default credentials (By GOOGLE_APPLICATION_CREDENTIALS envvar)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'storageBucket': c.G_BUCKET_NAME
})

db = firestore.client()
thumb_bucket = storage.bucket(c.G_BUCKET_NAME)

bclient = google.cloud.storage.Client()