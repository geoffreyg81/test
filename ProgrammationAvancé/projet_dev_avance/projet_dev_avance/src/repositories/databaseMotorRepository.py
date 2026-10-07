import mysql.connector
from core.interfaces.abstractMotorRepository import AbstractMotorRepository


class DatabaseMotorRepository(AbstractMotorRepository):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost", user="root", password="root81?", database="catalogue_db"
        )
        self.cursor = self.conn.cursor()
    def create(self, moteur):
        type_moteur = type(moteur).__name__
        taille_res = getattr(moteur, 'taille_reservoir', None)
        conso_carb = getattr(moteur, 'conso_carburant', None)
        cap_bat = getattr(moteur, 'capacite_batterie', None)
        conso_elec = getattr(moteur, 'conso_batterie', None)

        sql = "INSERT INTO motor (type_moteur, taille_reservoir, conso_carburant, capacite_batterie, conso_electrique) VALUES (%s, %s, %s, %s, %s)"
        val = (type_moteur, taille_res, conso_carb, cap_bat, conso_elec)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid
    def read(self) -> list:
        self.cursor.execute("SELECT * FROM motor")
        return self.cursor.fetchall()

    def update(self, id_moteur, moteur_modifie):
        taille_res = getattr(moteur_modifie, 'taille_reservoir', None)
        sql = "UPDATE motor SET taille_reservoir = %s WHERE id = %s"
        self.cursor.execute(sql, (taille_res, id_moteur))
        self.conn.commit()

    def delete(self, id_moteur):
        sql = "DELETE FROM motor WHERE id = %s"
        self.cursor.execute(sql, (id_moteur,))
        self.conn.commit()