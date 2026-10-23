import requests
import pymongo as pm
def request(URI):
    return(requests.get(URI))
def connect():
    client = pm.MongoClient("mongodb://localhost:27017/")
    return(client["starwars"])
db = connect()
x = True
count = 0
i = ""
shipList = []
while x:
    try:
        for ship in request("https://swapi.dev/api/starships"+i).json()["results"]:
            print(ship["name"])
            if ship["pilots"] is not None:
                pilots = []
                for pilot in ship["pilots"]:
                    response = request(pilot)
                    temp = db.characters.find_one({"name": response.json()["name"]},{"_id":1})
                    pilots.append(temp["_id"])
                    print("    pilot added:" + response.json()["name"])
                ship["pilots"] = pilots
            shipList.append(ship)
    except:
        x=False
    finally:
        print("page completed")
        count += 1
        i = "/?page=" + str(count)
db.starships.insert_many(shipList)