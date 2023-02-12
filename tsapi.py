from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)



class Ok(Resource):
    def get(self):
        return {"msg": "ok"}










api.add_resource(Ok, "/")







if __name__ == "__main__":
    app.run(debug = True)
