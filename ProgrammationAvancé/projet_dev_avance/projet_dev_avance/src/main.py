from models.motorisation.moteur import MoteurThermique
from models.vehicule.voiture import Vehicule

from repositories.databaseMotorRepository import DatabaseMotorRepository
from repositories.database_vehicule_repository import DatabaseVehiculeRepository

from services.motor_service import MotorService
from services.vehicule_service import VehiculeService

from controllers.catalog_controller import CatalogController

def main():
    print("==================================================")
    print("🔌 DÉMARRAGE DE L'API ET BRANCHEMENTS (INJECTION)")
    print("==================================================")

    # 1. Instanciation des Repositories (La couche BDD)
    motor_repo = DatabaseMotorRepository()
    vehicule_repo = DatabaseVehiculeRepository()

    # 2. Instanciation des Services (La couche Métier)
    # motor_service est lié à motor_repo
    motor_service = MotorService(motor_repo)
    # vehicule_service est lié à vehicule_repo ET motor_service
    vehicule_service = VehiculeService(vehicule_repo, motor_service)

    # 3. Instanciation du Controller (La couche Web/API)
    # L'API est liée au controller, et le controller interagit avec les services
    api_controller = CatalogController(vehicule_service, motor_service)

    print("✅ Serveur API prêt !")
    print("\n==================================================")
    print("🌐 SIMULATION DES REQUÊTES API")
    print("==================================================")

    # Création d'une donnée brute (comme si un client envoyait un JSON)
    moteur = MoteurThermique(taille_reservoir=50.0, conso_carburant=6.0)
    nouvelle_voiture = Vehicule(
        motorisation=moteur, marque="Audi", modele="A3",
        annee=2021, kilometrage=30000, volumeCoffre=380.0, categorie="Compacte"
    )

    # L'API reçoit une requête POST (Ajouter)
    print("-> Requête entrante : POST /vehicules")
    reponse_post = api_controller.api_post_vehicule(nouvelle_voiture)
    print(f"<- Réponse de l'API : {reponse_post}")

    print("\n-> Requête entrante : GET /vehicules")
    # L'API reçoit une requête GET (Lister)
    reponse_get = api_controller.api_get_vehicules()
    print(f"<- Réponse de l'API : Statut {reponse_get['status']}, Nombre d'éléments : {len(reponse_get['data'])}")

if __name__ == "__main__":
    main()