from flask_restful import Resource

class WorkoutREST(Resource):
    
    @staticmethod
    def get():
        return {'hello': 'world'}