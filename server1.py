#!flask/bin/python
from flask import Flask, jsonify, request, abort
# This is the mySQL connector
from santaDAO import santaDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/list')
def getAllPeople():
    results = santaDAO.getAllPeople()
    return jsonify(results)
    # Test in CURL
    # curl http://127.0.0.1:5000/list

@app.route('/workshop')
def getAllToys():
    results = santaDAO.getAllToys()
    return jsonify(results)
    # Test in CURL
    # curl http://127.0.0.1:5000/workshop

@app.route('/list/<int:id>')
def findPersonByID(id):
    foundPerson = santaDAO.findPersonByID(id)
    return jsonify(foundPerson)
    # Test in CURL
    # curl "http://127.0.0.1:5000/list/1"

@app.route('/workshop/<int:itemId>')
def findToysByID(itemId):
    foundToy = santaDAO.findToysByID(itemId)
    return jsonify(foundToy)
    # Test in CURL
    # curl "http://127.0.0.1:5000/workshop/1"


@app.route('/list', methods=['POST'])
def createPerson():
    
    if not request.json:
        abort(400)

    # Makes sure name  is a string
    if "name" in request.json and type(request.json["name"]) is not str:
        abort(400)
    # Makes sure gender is a either a boy or girl
    if "gender" in request.json and not (request.json["gender"] in ["not specified", "boy", "girl"]):
        abort(400)
    # Makes sure age is an integer
    if "age" in request.json and type(request.json["age"]) is not int:
        abort(400)
    # Makes sure Nice is either naughty or nice
    if "nice" in request.json and not (request.json["nice"] in ["naughty", "nice"]):
        abort(400)
    # Makes sure toy is a string
    if "toy" in request.json and type(request.json["toy"]) is not str:
        abort(400)
    # Makes sure Chimney is either yes or no
    if "chimney" in request.json and not (request.json["chimney"] in ["yes", "no"]):
        abort(400)
    # Makes sure toyok is either ready or not ready
    if "toyok" in request.json and not (request.json["toyok"] in ["ready", "not ready"]):
        abort(400)
    
    person = {
        "name":request.json["name"],
        "gender":request.json["gender"],
        "age": request.json["age"],
        "nice": request.json["nice"],
        "toy": request.json["toy"],
        "chimney": request.json["chimney"],
        "toyok": request.json["toyok"]
    }
    values = (person["name"], person["gender"], person["age"], person["nice"], person["toy"], person["chimney"], person["toyok"])
    newId =  santaDAO.createPerson(values)
    person['id']= newId
    return jsonify(person)
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/list"
    # curl -H "Content-Type:application/json" -X POST -d "{\"name\":\"Bernie\",\"gender\":\"male\",\"age\":8,\"nice\":1,\"toy\":\"skateboard\", \"chimney\":0, \"toyok\":0}" http://127.0.0.1:5000/list


@app.route('/workshop', methods=['POST'])
def createToy():
    if not request.json:
        abort(400)
    # Other checking - that it is properly formatted etc
    toy = {
        "item": request.json["item"],
        "stock": request.json["stock"]
    }
    values = (toy["item"], toy["stock"])
    newId = santaDAO.createToy(values)
    toy["itemId"] = newId
    return jsonify(toy)
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/workshop"
    # curl -H "Content-Type:application/json" -X POST -d "{\"item\":\"pogo stick\",\"stock\":3}" http://127.0.0.1:5000/workshop



@app.route('/list/<int:id>', methods=['PUT'])
def updatePerson(id):
    foundPerson = santaDAO.findPersonByID(id)
    if not foundPerson:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if "age" in reqJson and type(reqJson["age"]) is not int:
        abort(400)
    if "name" in reqJson:
        foundPerson["name"] = reqJson["name"]
    if "gender" in reqJson:
        foundPerson["gender"] = reqJson["gender"]
    if "age" in reqJson:
        foundPerson["age"] = reqJson["age"]
    if "nice" in reqJson:
        foundPerson["nice"] = reqJson["nice"]
    if "toy" in reqJson:
        foundPerson["toy"] = reqJson["toy"]
    if "chimney" in reqJson:
        foundPerson["chimney"] = reqJson["chimney"]
    if "toyok" in reqJson:
        foundPerson["toyok"] = reqJson["toyok"]
    values = (foundPerson["name"], foundPerson["gender"], foundPerson["age"],foundPerson["nice"], foundPerson["toy"], foundPerson["chimney"], foundPerson["toyok"],foundPerson["id"])
    # write to data
    santaDAO.updatePeople(values)
    return jsonify(foundPerson)
    # Test in CURL
    # curl -X PUT "http://127.0.0.1:5000/list/123"
    # curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"jenny\",\"gender\":\"girl\",\"age\":6, \"nice\":1, \"toy\": "\doll\", \"chimney\":1,\"toyok\":0}" http://127.0.0.1:5000/list/1


@app.route('/workshop/<int:itemId>', methods=['PUT'])
def updateToys(itemId):
    foundToy = santaDAO.findToysByID(itemId)
    if not foundToy:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    if "stock" in reqJson and type(reqJson["stock"]) is not int:
        abort(400)
    if "item" in reqJson:
        foundToy["item"] = reqJson["item"]
    if "stock" in reqJson:
        foundToy["stock"] = reqJson["stock"]
    values = (foundToy["item"], foundToy["stock"], foundToy["itemId"])
    # write to data
    santaDAO.updateToys(values)
    foundToy = santaDAO.findToysByID(itemId)
    return jsonify(foundToy)
    # Test in CURL
    # curl -X PUT "http://127.0.0.1:5000/workshop/123"
    # curl -i -H "Content-Type:application/json" -X PUT -d "{\"item\":\"spinning top\",\"stock\": 10}" http://127.0.0.1:5000/workshop/1


@app.route('/list/<int:id>', methods=['DELETE'])
def deletePerson(id):
    santaDAO.deletePerson(id)
    return jsonify({"done": True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/person/1"

@app.route('/workshop/<int:itemId>', methods=['DELETE'])
def deleteToys(itemId):
    santaDAO.deleteToys(itemId)
    return jsonify({"done":True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/workshop/1"

if __name__ == '__main__':
    app.run(debug=True)
