from flask_restful import Resource
from firebase_admin import firestore
from google.cloud import storage
from models import thumb_bucket

class MetaREST(Resource):
    
    @staticmethod
    def get():
        # Make firestore client
        fcl = firestore.client()

        response = {}
        
        # Gets the document, and transforms it to python dictionary
        level_doc_ref = fcl.collection('meta').document("meta") # This is only the reference. Haven't pulled from the server
        level_doc = level_doc_ref.get() # Here, data is actually pulled.

        if level_doc.exists:
            response = level_doc.to_dict()

            # Get versions
            response.get("version", "")
            
        return response
