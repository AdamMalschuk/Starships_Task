import unittest
import main
import pymongo as pm
import mongomock as mm

class RequestTest(unittest.TestCase):
    def test_Request_function(self):

        self.assertEqual(main.request("https://swapi.dev/api/starships").status_code, 200)  # add assertion here


class ConnectTest(unittest.TestCase):
    def test_ConnectTest_function(self):

        self.assertEqual(main.connect(), pm.MongoClient("mongodb://localhost:27017/")["starwars"])


class GetAndSetPilotsTest(unittest.TestCase):
    def test_GetAndSetPilots_function(self):
        ship = {
        "name": "Slave 1",
        "model": "Firespray-31-class patrol and attack",
        "manufacturer": "Kuat Systems Engineering",
        "cost_in_credits": "unknown",
        "length": "21.5",
        "max_atmosphering_speed": "1000",
        "crew": "1",
        "passengers": "6",
        "cargo_capacity": "70000",
        "consumables": "1 month",
        "hyperdrive_rating": "3.0",
        "MGLT": "70",
        "starship_class": "Patrol craft",
        "pilots": [
            "https://swapi.dev/api/people/22/"
        ],
        "films": [
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/5/"
        ],
        "created": "2014-12-15T13:00:56.332000Z",
        "edited": "2014-12-20T21:23:49.897000Z",
        "url": "https://swapi.dev/api/starships/21/"
        }
        client = mm.MongoClient()
        db = client["starwars"]
        collection = db["characters"]
        collection.insert_one({"name":"Boba Fett","_id":"1"})
        self.assertEqual(main.getAndSetPilots(ship,db)["pilots"][0], "1")
