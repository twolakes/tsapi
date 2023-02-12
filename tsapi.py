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
        if len(res) > 0:
            return {"data": res}
        
        return {"msg": "no data found"}

    def post(self):
        data = request.json
        res = self.db.add_item(data["item_name"])
        return ({"data": {res[0]: res[1]}})


class Item(Resource):

    def __init__(self):
        self.db = TSDb()

    def get(self, id):
        res = self.db.get_item(id)
        if res == None:
            return ({"msg": f"item {id} not found"})

        return ({"data": {res[0]: res[1]}})

    def put(self, id):
        data = request.json
        res = self.db.update_item(id, data['new_name'])
        if res == None:
            return ({"msg": f"item {id} not found"})
        
        return ({"data": {res[0]: res[1]}})

    def delete(self, id):
        res = self.db.del_item(id)
        if res == None:
            return ({"msg": f"item {id} not found"})

        return ({"msg": f"item {id} deleted"})







api.add_resource(Ok, "/")
api.add_resource(Items, "/items")
api.add_resource(Item, "/item/<int:id>")






if __name__ == "__main__":
    app.run(debug = True)
