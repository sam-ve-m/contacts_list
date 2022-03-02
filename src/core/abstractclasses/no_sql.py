from src.core.interfaces.repository.i_mongo import IMongo


class AbstractMongo(IMongo):

    def insert_update_one(self, data: dict) -> bool:
        pass

    def find_all(self) -> list:
        pass

    def find_one(self, identity: str) -> dict:
        pass

    def aggregate(self, pipeline: list) -> dict:
        pass

    def delete_one(self, identity: str) -> bool:
        pass
