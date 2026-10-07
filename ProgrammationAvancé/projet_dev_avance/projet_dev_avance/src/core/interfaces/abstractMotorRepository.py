from abc import ABC, abstractmethod

class AbstractMotorRepository(ABC):
    @abstractmethod
    def create(self, motor):
        pass

    @abstractmethod
    def read(self) -> list:
        pass

    @abstractmethod
    def update(self, id_motor, motor_modifie):
        pass

    @abstractmethod
    def delete(self, id_motor):
        pass