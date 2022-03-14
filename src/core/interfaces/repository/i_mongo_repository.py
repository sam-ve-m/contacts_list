from abc import ABC

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


class IMongo(ABC):
    DATABASE: str
    COLLECTION: str

    def __init__(self, infrastructure: MongoClient):
        connection = infrastructure
        database = connection[self.DATABASE]
        self.collection = database[self.COLLECTION]

    def insert_update_one(self, data: dict) -> bool:
        try:
            if not self.collection.insert_one(data):
                return False                                    # TODO: Separate insert and update
            return True
        except DuplicateKeyError:
            return False

    def find_all(self) -> list:
        return self.collection.find({})

    def find_one(self, identity: str) -> dict:
        return self.collection.find_one({"_id": identity})

    def aggregate(self, pipeline: list) -> dict:
        pass

    def delete_one(self, identity: str) -> bool:
        if not self.collection.find_one_and_delete({"_id": identity}):
            return False                                    # TODO: Introduce cache
        return True