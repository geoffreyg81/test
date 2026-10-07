from abc import ABC, abstractmethod
class Repository(ABC):
    @abstractmethod
    def ajouterRepository(self, vehicule):
        pass
    @abstractmethod
    def lister(self) -> list:
        pass