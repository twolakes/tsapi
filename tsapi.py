from flask import Flask, request
from flask_restful import Resource, Api
from resources.items import Items
from resources.item import Item

from db import TSDb



app = Flask(__name__)
api = Api(app)



class Ok(Resource):

    def get(self):
        return {"msg": "ok"}






api.add_resource(Ok, "/")
api.add_resource(Items, "/items")
api.add_resource(Item, "/item/<int:id>")






if __name__ == "__main__":
    app.run(debug = True)
