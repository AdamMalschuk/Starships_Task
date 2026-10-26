import requests
import pymongo as pm
#runs an API call
def request(URI):
    return(requests.get(URI))
#connects to mongodb database
def connect():
    client = pm.MongoClient("mongodb://localhost:27017/")
    return(client["starwars"])
db = connect()
#holds while loop open
x = True
#count for adding into request for different pages
count = 0
#i set to empty string for first pass to access page 1
i = ""
#declaring the ship list to populated with the results of the API
shipList = []
while x:
    #tries the API call
    try:
        for ship in request("https://swapi.dev/api/starships"+i).json()["results"]:
            print(ship["name"])
            if ship["pilots"] is not None:
                pilots = []
                for pilot in ship["pilots"]:
                    #follows the pilot link
                    response = request(pilot)
                    #searches for the pilot in the mongo database
                    temp = db.characters.find_one({"name": response.json()["name"]},{"_id":1})
                    pilots.append(temp["_id"])
                    #shows the pilot added with some indentation for easier reading
                    print("    pilot added:" + response.json()["name"])
                ship["pilots"] = pilots
            shipList.append(ship)
    #if the page being accessed doesn't exist then it ends the while loop
    except:
        x=False
    #displays the end of the page and creates the string to add to get the next page
    finally:
        print("page completed")
        count += 1
        i = "/?page=" + str(count)
db.starships.insert_many(shipList)