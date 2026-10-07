from core.interfaces.Motorisation import Motorisation
from utils.decorateur import valider


class MoteurThermique(Motorisation):
    def __init__(self, taille_reservoir: float, conso_carburant: float):
        self.taille_reservoir = taille_reservoir
        self.conso_carburant = conso_carburant

    @property
    def taille_reservoir(self):
        return self._taille_reservoir

    @taille_reservoir.setter
    @valider
    def taille_reservoir(self, value):
        self._taille_reservoir = value

    @property
    def conso_carburant(self):
        return self._conso_carburant

    @conso_carburant.setter
    @valider
    def conso_carburant(self, value):
        self._conso_carburant = value

    def afficher_caracteristique(self) -> str:
        return f"Taille du reservoir: {self.taille_reservoir}L, Consommation: {self.conso_carburant}L/100km"


class MoteurElectrique(Motorisation):
    def __init__(self, capacite_batterie: float, conso_batterie: float):
        self.capacite_batterie = capacite_batterie
        self.conso_batterie = conso_batterie

    @property
    def capacite_batterie(self):
        return self._capacite_batterie

    @capacite_batterie.setter
    @valider
    def capacite_batterie(self, value):
        self._capacite_batterie = value

    @property
    def conso_batterie(self):
        return self._conso_batterie

    @conso_batterie.setter
    @valider
    def conso_batterie(self, value):
        self._conso_batterie = value

    def afficher_caracteristique(self) -> str:
        return f"Capacite batterie: {self.capacite_batterie}kWh, Consommation: {self.conso_batterie}kWh/100km"


class MoteurHybride(MoteurThermique, MoteurElectrique):
    def __init__(self, taille_reservoir: float, conso_carburant: float, taillebatterie: float, conso_batterie: float):
        # En appelant les __init__ des parents, les setters des parents s'activent automatiquement !
        MoteurThermique.__init__(self, taille_reservoir, conso_carburant)
        MoteurElectrique.__init__(self, taillebatterie, conso_batterie)

    def afficher_caracteristique(self) -> str:
        return (f"Reservoir: {self.taille_reservoir}L, Conso carburant: {self.conso_carburant}L/100km, "
                f"Batterie: {self.capacite_batterie}kWh, Conso electrique: {self.conso_batterie}kWh/100km")