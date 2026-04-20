import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r") as f:
            config = json.load(f)

        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection

    def insert_salle(self, salle):
        connection = self.get_connection()
        curseur = connection.cursor()
        requete = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
        valeurs = (salle.code, salle.description, salle.categorie, salle.capacite)
        curseur.execute(requete, valeurs)
        connection.commit()
        curseur.close()
        connection.close()

    def update_salle(self, salle):
        connection = self.get_connection()
        curseur = connection.cursor()
        requete = "UPDATE salle SET description=%s, categorie=%s, capacite=%s WHERE code=%s"
        valeurs = (salle.description, salle.categorie, salle.capacite, salle.code)
        curseur.execute(requete, valeurs)
        connection.commit()
        curseur.close()
        connection.close()

    def delete_salle(self, code):
        connection = self.get_connection()
        curseur = connection.cursor()
        requete = "DELETE FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        connection.commit()
        curseur.close()
        connection.close()

    def get_salle(self, code):
        connection = self.get_connection()
        curseur = connection.cursor()
        requete = "SELECT * FROM salle WHERE code=%s"
        curseur.execute(requete, (code,))
        resultat = curseur.fetchone()
        curseur.close()
        connection.close()

        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
        return None

    def get_salles(self):
        connection = self.get_connection()
        curseur = connection.cursor()
        requete = "SELECT * FROM salle"
        curseur.execute(requete)
        resultats = curseur.fetchall()
        curseur.close()
        connection.close()

        liste = []
        for row in resultats:
            liste.append(Salle(row[0], row[1], row[2], row[3]))
        return liste