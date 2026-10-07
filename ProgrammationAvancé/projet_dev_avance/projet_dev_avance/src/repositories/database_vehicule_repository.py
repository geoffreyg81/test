import mysql.connector
from core.interfaces.abstractVehiculeRepository import AbstractVehiculeRepository

class DatabaseVehiculeRepository(AbstractVehiculeRepository):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="root81?", database="catalogue_db"
        )
        self.cursor = self.conn.cursor()

    # C : CREATE (Insert into)
    # Remarque : on doit passer l'ID du moteur pour faire le lien (la clé étrangère) !
    def create(self, vehicule, motor_id):
        sql = "INSERT INTO car (marque, modele, annee, kilometrage, volume_coffre, categorie, motor_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (vehicule.marque, vehicule.modele, vehicule.annee, vehicule.kilometrage, vehicule.volumeCoffre, vehicule.categorie, motor_id)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print(f"[BDD] Voiture {vehicule.marque} ajoutée !")

    # R : READ (Select * from)
    def read(self) -> list:
        # Comme demandé par le prof : le fameux Select *
        self.cursor.execute("SELECT * FROM car")
        return self.cursor.fetchall()

    # U : UPDATE
    def update(self, id_vehicule, vehicule_modifie):
        sql = """
            UPDATE car 
            SET marque = %s, modele = %s, annee = %s, kilometrage = %s, volume_coffre = %s, categorie = %s 
            WHERE id = %s
        """
        val = (vehicule_modifie.marque, vehicule_modifie.modele, vehicule_modifie.annee,
               vehicule_modifie.kilometrage, vehicule_modifie.volumeCoffre, vehicule_modifie.categorie, id_vehicule)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print(f"[BDD] Voiture {id_vehicule} mise à jour !")

    # D : DELETE
    def delete(self, id_vehicule):
        sql = "DELETE FROM car WHERE id = %s"
        self.cursor.execute(sql, (id_vehicule,))
        self.conn.commit()
        print(f"[BDD] Voiture {id_vehicule} supprimée !")