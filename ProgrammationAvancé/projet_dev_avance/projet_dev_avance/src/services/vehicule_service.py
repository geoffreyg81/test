from core.interfaces.abstractVehiculeRepository import AbstractVehiculeRepository
from services.motor_service import MotorService


class VehiculeService:
    def __init__(self, vehicule_repo: AbstractVehiculeRepository, motor_service: MotorService):
        self.vehicule_repo = vehicule_repo
        self.motor_service = motor_service

    def create_vehicule(self, vehicule):
        motor_id = self.motor_service.create_moteur(vehicule.motorisation)
        self.vehicule_repo.create(vehicule, motor_id)
    def get_vehicules(self):
        return self.vehicule_repo.read()

    def update_vehicule(self, id_vehicule, vehicule_modifie):
        self.vehicule_repo.update(id_vehicule, vehicule_modifie)

    def delete_vehicule(self, id_vehicule):
        """Supprime un véhicule du catalogue"""
        self.vehicule_repo.delete(id_vehicule)