import pymongo
from src.core.infrastructure.i_mongo import IMongoDBInfrastructure
from src.utils.env_config import config


class MongoDBInfrastructure(IMongoDBInfrastructure):
    connection: any = None

    @staticmethod
    def get_connection(
            url: str = config("MONGO_HOST"),
            port=config("MONGO_PORT"),
            username: str = config("MONGO_USER"),
            password: str = config("MONGO_PASS")
    ) -> any:
        try:
            host = f"mongodb://{username}:{password}@{url}:{port}"
            connection = pymongo.MongoClient(host)
            return connection
        except Exception as error:
            raise error

    @classmethod
    def get_singleton_connection(
            cls,
            url: str = config("MONGO_HOST"),
            port: int = config("MONGO_PORT"),
            username: str = config("MONGO_USER"),
            password: str = config("MONGO_PASS")
    ) -> any:
        if cls.connection is None:
            cls.connection = cls.get_connection(url, port, username, password)
        return cls.connection
