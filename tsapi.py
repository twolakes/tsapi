from flask import Flask, request
from flask_restful import Resource, Api

from db import TSDb



app = Flask(__name__)
api = Api(app)



class Ok(Resource):
    def get(self):
        return {"msg": "ok"}


class Items(Resource):

    def __init__(self):
        self.db = TSDb()

    def get(self):
        res = self.db.get_items()
        return {"data": res}







api.add_resource(Ok, "/")
api.add_resource(Items, "/items")






if __name__ == "__main__":
    app.run(debug = True)
