from flask_restful import Resource
from firebase_admin import firestore
from google.cloud import storage
from models import thumb_bucket

class WorkoutREST(Resource):

    thumbnailsite = "https://storage.googleapis.com/{bucketname}/{thumbname}"
    
    @staticmethod
    def get(pack):
        # Make firestore client
        fcl = firestore.client()

        response = {"levels": ""}
        
        # Gets the document, and transforms it to python dictionary
        level_doc_ref = fcl.collection('workouts').document(pack) # This is only the reference. Haven't pulled from the server
        level_doc = level_doc_ref.get() # Here, data is actually pulled.

        if level_doc.exists:
            response = level_doc.to_dict()

            # Replace every thumbnail with bucket link.
            for level in response["levels"]:
                file_name = level.get("thumbnail")
                # Check whether the blob exist in the bucket

                level['thumbnail'] = WorkoutREST.thumbnailsite.format(
                    bucketname=thumb_bucket.name,
                    thumbname=((file_name if storage.Blob(file_name, thumb_bucket).exists() else "default.png") if file_name else "default.png")
                )
            
        return response