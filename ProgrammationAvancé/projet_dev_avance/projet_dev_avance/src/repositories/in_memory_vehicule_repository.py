from core.interfaces.abstractVehiculeRepository import AbstractVehiculeRepository

class InMemoryVehiculeRepository(AbstractVehiculeRepository):
    def __init__(self):
        self.tab = []

    def create(self, vehicule):
        self.tab.append(vehicule)
        print("Véhicule créé en mémoire.")

    def read(self) -> list:
        return self.tab

    def update(self, index, vehicule_modifie):
        if 0 <= index < len(self.tab):
            self.tab[index] = vehicule_modifie
            print("Véhicule mis à jour.")
        else:
            print("Erreur : Véhicule introuvable.")

    def delete(self, index):
        if 0 <= index < len(self.tab):
            vehicule_supprime = self.tab.pop(index)
            print("Véhicule supprimé.")
        else:
            print("Erreur : Véhicule introuvable.")