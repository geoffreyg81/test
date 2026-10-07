from abc import ABC, abstractmethod
class Motorisation(ABC):
    @abstractmethod
    def afficher_caracteristique(self) -> str:
        pass