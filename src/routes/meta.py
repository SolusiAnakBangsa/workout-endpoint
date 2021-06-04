from flask import Blueprint
from flask_restful import Api

from rest import MetaREST

META_BL = Blueprint("meta", __name__, url_prefix="/app/meta")
api = Api(META_BL)
api.add_resource(MetaREST, "")