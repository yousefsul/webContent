import logging
from pymongo import MongoClient

MONGO_CLIENT = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"


class ConnectMongoDB:
    def __init__(self):
        try:
            self.mongo_client = MongoClient(MONGO_CLIENT)
            self.test_db = self.mongo_client.testDB
        except ConnectionError:
            logging.error("constructor Method:         Error while connect to mongoDB")
            print("Error while connection to mongoDB")

    def connect_claim_status_codes_collection_collection(self):
        self.claim_status_codes_collection = self.test_db.ClaimStatusCodesCol

    def connect_to_claim_status_category_codes_collection(self):
        self.claim_status_category_codes_collection = self.test_db.ClaimStatusCategoryCodesCol

    def insert_to_claim_status_codes_collection(self, result):
        try:
            self.claim_status_codes_collection.insert(result)
        except Exception as e:
            print("An Exception occurred ", e)

    def insert_to_claim_status_category_codes_collection_collection(self, result):
        try:
            self.claim_status_category_codes_collection.insert(result)
        except Exception as e:
            print("An Exception occurred ", e)
