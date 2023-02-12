from flask import Flask, request
from flask_restful import Resource, Api

from db import TSDb



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