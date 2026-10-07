from core.interfaces.abstractVehiculeRepository import AbstractVehiculeRepository
from core.interfaces.abstractMotorRepository import AbstractMotorRepository


class CatalogService:
    def __init__(self, vehicule_repo: AbstractVehiculeRepository, motor_repo: AbstractMotorRepository):
        self.vehicule_repo = vehicule_repo
        self.motor_repo = motor_repo

    def ajouter_vehicule(self, vehicule):
        motor_id = self.motor_repo.create(vehicule.motorisation)

        self.vehicule_repo.create(vehicule, motor_id)

    def lister_vehicules(self):
        return self.vehicule_repo.read()