from flask import Flask, request
from flask_restful import Resource, Api

from db import TSDb



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
