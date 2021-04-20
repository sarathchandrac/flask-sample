from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")

db = client.aNewDB
UserNum = db["UserNum"]

UserNum.insert({
    'num_of_users': 0
})

items = []
class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, { "$set" :{"num_of_users" : new_num}})
        return UserNum.find({})[0]['num_of_users']

def checkPostedData(postedData, functionName):
    if(functionName == "add" or functionName == "subtract" or functionName == "multiply"):
        if "x" not in postedData or "y" not in postedData:
            return 301 # missing required parameters
        else:
            return 200
    elif(functionName == "division"):
        if "x" not in postedData or "y" not in postedData:
            return 301 # missing required parameters
        elif int(postedData["y"])==0:
            return 302 # invalid parameter value
        else:
            return 200

class Add(Resource):
    def post(self):
        postedData = request.get_json()
        return 2
class Subtract(Resource):
    def post(self):
        postedData = request.get_json()
        return 2
class Multiply(Resource):
    def post(self):
        postedData = request.get_json()
        return 2
class Devide(Resource):
    def post(self):
        postedData = request.get_json()
        return 2


class Student(Resource):
    def get(self, name):
        return {'student': name}
class Item(Resource):
    def get(self, name):
        item = get_item(name, items)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        data = request.get_json()
        if get_item(name, items) is not None:
            return {'message': "An Item with '{}' already exists".format(name)}, 401

        item = {'name': name, 'price': data['price']}
        print(item)
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return {'items': items}
def get_item(name, items):
    return next(filter(lambda x:  x['name'] == name if 'name' in x else False, items), None)


api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Visit, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)

# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()
