from core.interfaces.abstractMotorRepository import AbstractMotorRepository

class MotorService:
    def __init__(self, motor_repo: AbstractMotorRepository):
        self.motor_repo = motor_repo

    def create_moteur(self, moteur):
        return self.motor_repo.create(moteur)

    def get_moteurs(self):
        return self.motor_repo.read()

    def update_moteur(self, id_moteur, moteur_modifie):
        self.motor_repo.update(id_moteur, moteur_modifie)

    def delete_moteur(self, id_moteur):
        self.motor_repo.delete(id_moteur)