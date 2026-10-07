from src.core.interfaces.Motorisation import Motorisation
from utils.decorateur import valider


class Vehicule:
    def __init__(self, motorisation: Motorisation, marque: str, modele: str, annee: int, kilometrage: int,
                 volumeCoffre: float, categorie: str):
        self.motorisation = motorisation
        self.marque = marque
        self.modele = modele
        self.categorie = categorie

        # Attributs avec garde du corps (setters)
        self.annee = annee
        self.kilometrage = kilometrage
        self.volumeCoffre = volumeCoffre

    # --- SETTERS SÉCURISÉS ---

    @property
    def annee(self):
        return self._annee

    @annee.setter
    @valider
    def annee(self, value):
        self._annee = value

    @property
    def kilometrage(self):
        return self._kilometrage

    @kilometrage.setter
    @valider
    def kilometrage(self, value):
        self._kilometrage = value

    @property
    def volumeCoffre(self):
        return self._volumeCoffre

    @volumeCoffre.setter
    @valider
    def volumeCoffre(self, value):
        self._volumeCoffre = value

    # -------------------------

    def afficher_caracteristique(self) -> str:
        return (
            f"Details moteur [{self.motorisation.afficher_caracteristique()}], "
            f"Marque: {self.marque}, Modele: {self.modele}, Annee: {self.annee}, "
            f"Kilometrage: {self.kilometrage}, Coffre: {self.volumeCoffre}L, "
            f"Categorie: {self.categorie}"
        )