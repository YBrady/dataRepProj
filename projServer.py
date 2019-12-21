#!flask/bin/python
from flask import Flask, jsonify, request, abort
# This is the mySQL connector
from santaDAO import santaDAO
import projApi

app = Flask(__name__, static_url_path='', static_folder='.')

#   Used to create the naughty and nice lists
@app.route('/list')
def getAllPeople():
    results = santaDAO.getAllPeople()
    return jsonify(results)
    # Test in CURL
    # curl http://127.0.0.1:5000/list

# To check if a person is naughty or nice
@app.route('/list/<name>')
def getStatusPerson(name):
    results = santaDAO.checkPersonByName(name)
    return results
    # Test in CURL
    # curl http://127.0.0.1:5000/list/John

# Having multiple calls to same route was problematic
# So this is my workaround
@app.route('/workshop/<what>')
# Same function for all SQL GET queries for the workshop 
def getAllToys(what):
    # Just looking to update the toys list
    if what == "stock":
        results = santaDAO.getWorkshop("stock")
        return jsonify(results)
    # Looking to update the Toys to Make list
    if what == "make":
        results = santaDAO.getWorkshop("make")
        return jsonify(results)
    # Looking to update both
    if what == "both":
        results = santaDAO.getWorkshop("both")
        return(jsonify(results))
    # Test in CURL
    # curl http://127.0.0.1:5000/workshop/both


# Returns one person if searched by id
@app.route('/list/<int:id>')
def findPersonByID(id):
    foundPerson = santaDAO.findPersonByID(id)
    return jsonify(foundPerson)
    # Test in CURL
    # curl "http://127.0.0.1:5000/list/1"

# Finds a toy by id
@app.route('/workshop/<int:itemId>')
def findToysByID(itemId):
    foundToy = santaDAO.findToysByID(itemId)
    return jsonify(foundToy)
    # Test in CURL
    # curl "http://127.0.0.1:5000/workshop/1"

# When adding a new person to the list
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
    # Formats the person data
    person = {
        "name":request.json["name"],
        "gender":request.json["gender"],
        "age": request.json["age"],
        "nice": request.json["nice"],
        "toy": request.json["toy"],
        "chimney": request.json["chimney"],
    }
    # Assembles the values for the insert
    values = (person["name"], person["gender"], person["age"], person["nice"], person["toy"], person["chimney"])
    # Performs the addition
    newId =  santaDAO.createPerson(values)
    # Get the id of the person
    person['id']= newId
    # Return the person detauls complete with id
    return jsonify(person)
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/list"
    # curl -H "Content-Type:application/json" -X POST -d "{\"name\":\"Bernie\",\"gender\":\"male\",\"age\":8,\"nice\":1,\"toy\":\"skateboard\", \"chimney\":0, \"toyok\":0}" http://127.0.0.1:5000/list

# Used to create a toy
@app.route('/workshop', methods=['POST'])
def createToy():
    if not request.json:
        abort(400)
    # Makes sure item is a string
    if "item" in request.json and type(request.json["item"]) is not str:
        abort(400)
    # Makes sure stock is an integer
    if "stock" in request.json and type(request.json["stock"]) is not int:
        abort(400)
    # Put the info together
    toy = {
        "item": request.json["item"],
        "stock": request.json["stock"]
    }
    # Add the values for the SQL string
    values = (toy["item"], toy["stock"])
    # Add the toy to the database
    newId = santaDAO.createToy(values)
    # Get the id
    toy["itemId"] = newId
    # Return the complet info including id
    return jsonify(toy)
    # Test in CURL
    # curl -X POST "http://127.0.0.1:5000/workshop"
    # curl -H "Content-Type:application/json" -X POST -d "{\"item\":\"pogo stick\",\"stock\":3}" http://127.0.0.1:5000/workshop


# To update a persons details
@app.route('/list/<int:id>', methods=['PUT'])
def updatePerson(id):
    # Get ther person
    foundPerson = santaDAO.findPersonByID(id)
    # Error if the person was not found
    if not foundPerson:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    # Does the checks of the data again
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
    values = (foundPerson["name"], foundPerson["gender"], foundPerson["age"],foundPerson["nice"], foundPerson["toy"], foundPerson["chimney"],foundPerson["id"])
    # write to data
    santaDAO.updatePeople(values)
    return jsonify(foundPerson)
    # Test in CURL
    # curl -X PUT "http://127.0.0.1:5000/list/123"
    # curl -i -H "Content-Type:application/json" -X PUT -d "{\"name\":\"jenny\",\"gender\":\"girl\",\"age\":6, \"nice\":1, \"toy\": "\doll\", \"chimney\":1,\"toyok\":0}" http://127.0.0.1:5000/list/1


# To update a toys details
@app.route('/workshop/<int:itemId>', methods=['PUT'])
def updateToys(itemId):
    foundToy = santaDAO.findToysByID(itemId)
    # Error if not found
    if not foundToy:
        abort(404)
    if not request.json:
        abort(400)
    reqJson = request.json
    # Makes sure stock is an integer
    if "stock" in reqJson and type(reqJson["stock"]) is not int:
        abort(400)
    # Does the replacing
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

# Deletes a person from the table
@app.route('/list/<int:id>', methods=['DELETE'])
def deletePerson(id):
    santaDAO.deletePerson(id)
    return jsonify({"done": True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/person/1"

# Deletes a toy from the table
@app.route('/workshop/<int:itemId>', methods=['DELETE'])
def deleteToys(itemId):
    santaDAO.deleteToys(itemId)
    return jsonify({"done":True})
    # Test in CURL
    # curl -X DELETE "http://127.0.0.1:5000/workshop/1"

# Gets the api data
@app.route('/other/<what>')
def updateApiData(what):
    # If they are looking for the weather update - do this 
    if what == "weather":   
        # Get Weather
        forecastList = ["past", "current", "future"]
        weatherResults = []
        # Gather ther results for each of the times
        for forecast in forecastList:
            weatherResults.append(projApi.getForecast(forecast))
        #return the jsonified reaults
        return jsonify(weatherResults)
    # If they are looking for mail 
    if what == "mail":
        # Get mails
        messages = projApi.getMail()
        return jsonify(messages)
    # Test in CURL
    # curl http://127.0.0.1:5000/other/weather
    # curl http://127.0.0.1:5000/other/mail

if __name__ == '__main__':
    app.run(debug=True)
