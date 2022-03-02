from abc import ABC, abstractmethod


class IMongo(ABC):
    @abstractmethod
    def insert_update_one(self, data: dict) -> bool:
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass

    @abstractmethod
    def find_one(self, identity: str) -> dict:
        pass

    @abstractmethod
    def aggregate(self, pipeline: list) -> dict:
        pass

    @abstractmethod
    def delete_one(self, identity: str) -> bool:
        pass
