from src.infrastructure.mongo import MongoDBInfrastructure

mongo_connection = MongoDBInfrastructure.get_connection()

a = 1