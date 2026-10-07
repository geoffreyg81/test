# --- IMPORTS ---
# On importe les modèles (Étape 3)
from models.motorisation.moteur import MoteurThermique, MoteurElectrique, MoteurHybride
from models.vehicule.voiture import Vehicule

# NOUVEAUX IMPORTS DES REPOSITORIES CRUD (Étape 4)
from repositories.databaseMotorRepository import DatabaseMotorRepository
from repositories.database_vehicule_repository import DatabaseVehiculeRepository

# On importe le Service (Étape 5)
from services.catalog_service import CatalogService


def main():
    print("==================================================")
    print("🏁 TEST ÉTAPE 3 : Création des Modèles (Composition)")
    print("==================================================")

    # 1. On crée un moteur seul
    moteur_v8 = MoteurThermique(taille_reservoir=60.0, conso_carburant=8.5)

    # 2. On crée la voiture en lui donnant le moteur
    voiture_thermique = Vehicule(
        motorisation=moteur_v8,
        marque="Renault",
        modele="Megane",
        annee=2020,
        kilometrage=45000,
        volumeCoffre=384.0,
        categorie="Berline"
    )

    print("✅ Voiture thermique créée avec succès !")
    print(voiture_thermique.afficher_caracteristique())
    print("\n")

    print("==================================================")
    print("📁 TEST CRUD : Stockage via les nouveaux Repositories")
    print("==================================================")

    # 1. On crée nos deux Repositories connectés à la base de données
    motor_repo = DatabaseMotorRepository()
    vehicule_repo = DatabaseVehiculeRepository()

    # 2. On injecte les deux dans notre service
    mon_catalogue = CatalogService(vehicule_repo, motor_repo)

    # 3. On ajoute notre voiture (le service va s'occuper de créer le moteur puis la voiture)
    print("Tentative d'ajout d'une voiture thermique...")
    mon_catalogue.ajouter_vehicule(voiture_thermique)
    print("Tentative d'ajout d'une voiture hybride...")

    # 1. On crée le moteur hybride
    moteur_hyb = MoteurHybride(
        taille_reservoir=43.0,
        conso_carburant=4.5,
        taillebatterie=8.8,
        conso_batterie=12.0
    )

    # 2. On crée la voiture
    voiture_hybride = Vehicule(
        motorisation=moteur_hyb,
        marque="Toyota",
        modele="Prius",
        annee=2022,
        kilometrage=25000,
        volumeCoffre=343.0,
        categorie="Berline"
    )

    # 3. On l'ajoute au catalogue
    mon_catalogue.ajouter_vehicule(voiture_hybride)
    # 4. On teste le READ (Lecture)
    print("\n✅ Contenu brut de la table 'car' (READ) :")
    liste_brute = mon_catalogue.lister_vehicules()
    for ligne in liste_brute:
        print(ligne)

    print("\n==================================================")
    print("🛡️ TEST ÉTAPE 6 : Utilitaires (Décorateurs)")
    print("==================================================")

    # Test du validateur avec une valeur aberrante
    print("Tentative de création/ajout d'un véhicule avec un kilométrage invalide (-500 km) :")
    try:
        voiture_invalide = Vehicule(
            motorisation=moteur_v8,
            marque="Peugeot",
            modele="308",
            annee=2021,
            kilometrage=-500,  # Valeur volontairement fausse pour déclencher le décorateur !
            volumeCoffre=412.0,
            categorie="Compacte"
        )
        mon_catalogue.ajouter_vehicule(voiture_invalide)

        print("❌ ERREUR : La voiture a été ajoutée alors qu'elle a un kilométrage négatif. Vérifie ton validateur !")
    except Exception as e:
        # Si le validateur fonctionne, il va lever une exception
        print(f"✅ Succès du validateur ! L'action a été bloquée avec l'erreur : {e}")


if __name__ == "__main__":
    main()