from abc import ABC, abstractmethod
from typing import Any


class IList(ABC):
    @abstractmethod
    def get_list(self) -> dict:
        pass
