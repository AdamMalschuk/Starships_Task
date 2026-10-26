import unittest
from typing import Mapping

import pymongo as pm

class QueryTest(unittest.TestCase):
    def test_correct_amount_of_ships(self):
        client = pm.MongoClient("mongodb://localhost:27017/")
        db = client["starwars"]
        self.assertEqual(db.starships.count_documents({}), 36)
        client.close()

class QueryTest2(unittest.TestCase):
    def test_correct_referencing(self):
        client = pm.MongoClient("mongodb://localhost:27017/")
        db = client["starwars"]
        query = list(db.starships.aggregate([{"$match": {"name":"Slave 1"}},{"$lookup":{"from":"characters","localField":"pilots","foreignField":"_id","as":"pilot"}}]))
        self.assertEqual(query[0]["pilot"][0]["name"], "Boba Fett")
        client.close()

