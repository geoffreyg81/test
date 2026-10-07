from src.core.interfaces.Repository import Repository
class MoteurRepository(Repository):
    def __init__(self):
        self.catalogue = []

    # Tu dois obligatoirement créer la méthode avec le nom EXACT demandé par l'erreur
    def ajouterRepository(self, moteur):
        self.catalogue.append(moteur)

    # N'oublie pas l'autre méthode si elle est aussi dans ton interface !
    def lister(self) -> list:
        return self.catalogue