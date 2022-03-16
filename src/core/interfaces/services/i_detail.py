from abc import ABC, abstractmethod


class IDetail(ABC):
    @abstractmethod
    def get_detail(self) -> dict:
        pass
