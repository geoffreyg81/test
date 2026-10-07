import mysql.connector
from repositories.moteurRepository import MoteurRepository


class MySQLRepository(MoteurRepository):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",  # <-- On utilise root
            password="root81?",  # <-- Mets le même mot de passe que dans HeidiSQL !
            database="catalogue_db"
        )
        self.cursor = self.conn.cursor()

    def ajouterRepository(self, vehicule):
        moteur = vehicule.motorisation
        type_moteur = type(moteur).__name__

        taille_res = getattr(moteur, 'taille_reservoir', None)
        conso_carb = getattr(moteur, 'conso_carburant', None)
        cap_bat = getattr(moteur, 'capacite_batterie', None)
        conso_elec = getattr(moteur, 'conso_batterie', None)

        sql_moteur = "INSERT INTO motor (type_moteur, taille_reservoir, conso_carburant, capacite_batterie, conso_electrique) VALUES (%s, %s, %s, %s, %s)"
        val_moteur = (type_moteur, taille_res, conso_carb, cap_bat, conso_elec)

        self.cursor.execute(sql_moteur, val_moteur)
        motor_id = self.cursor.lastrowid

        sql_voiture = "INSERT INTO car (marque, modele, annee, kilometrage, volume_coffre, categorie, motor_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val_voiture = (vehicule.marque, vehicule.modele, vehicule.annee, vehicule.kilometrage,
                       getattr(vehicule, 'volumeCoffre', 0.0), vehicule.categorie, motor_id)

        self.cursor.execute(sql_voiture, val_voiture)

        self.conn.commit()
        print(f"[BDD] Véhicule {vehicule.marque} {vehicule.modele} sauvegardé en base de données !")

    def lister(self) -> list:
        # On va chercher les voitures et leurs moteurs avec une jointure SQL
        requete = """
                  SELECT car.marque, \
                         car.modele, \
                         car.annee, \
                         car.kilometrage, \
                         car.volume_coffre, \
                         car.categorie,
                         motor.type_moteur, \
                         motor.taille_reservoir, \
                         motor.conso_carburant, \
                         motor.capacite_batterie, \
                         motor.conso_electrique
                  FROM car
                           INNER JOIN motor ON car.motor_id = motor.id \
                  """
        self.cursor.execute(requete)
        lignes = self.cursor.fetchall()

        catalogue = []
        for ligne in lignes:
            # On décompose la ligne de résultat de la BDD
            marque, modele, annee, km, coffre, cat, type_mot, res, conso_carb, bat, conso_elec = ligne

            # 1. On recrée l'objet Moteur correspondant
            if type_mot == 'MoteurThermique':
                from models.motorisation.moteur import MoteurThermique
                moteur = MoteurThermique(res, conso_carb)
            elif type_mot == 'MoteurElectrique':
                from models.motorisation.moteur import MoteurElectrique
                moteur = MoteurElectrique(bat, conso_elec)
            else:
                from models.motorisation.moteur import MoteurHybride
                moteur = MoteurHybride(res, conso_carb, bat, conso_elec)

            # 2. On recrée l'objet Vehicule
            from models.vehicule.voiture import Vehicule
            voiture = Vehicule(moteur, marque, modele, annee, km, coffre, cat)
            catalogue.append(voiture)

        return catalogue