from flask import Blueprint
from flask_restful import Api

from rest import WorkoutREST

WORKOUT_BL = Blueprint("workout", __name__, url_prefix="/workouts/workout")
api = Api(WORKOUT_BL)
api.add_resource(WorkoutREST, "/levelpack/<string:pack>")