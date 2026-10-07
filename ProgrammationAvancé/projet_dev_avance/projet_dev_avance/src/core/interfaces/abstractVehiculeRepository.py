from abc import ABC, abstractmethod

class AbstractVehiculeRepository(ABC):
    @abstractmethod
    def create(self, vehicule):
        pass

    @abstractmethod
    def read(self) -> list:
        pass

    @abstractmethod
    def update(self, id_vehicule, vehicule_modifie):
        pass

    @abstractmethod
    def delete(self, id_vehicule):
        pass