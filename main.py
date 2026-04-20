from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# test connexion
conn = dao.get_connection()
print("Connexion réussie")
conn.close()

# ajouter
s1 = Salle("S001", "Salle reseau", "Laboratoire", 20)
dao.insert_salle(s1)
print("Salle ajoutée")

# modifier
s1_mod = Salle("S001", "Salle reseau A", "Laboratoire", 25)
dao.update_salle(s1_mod)
print("Salle modifiée")

# rechercher
salle = dao.get_salle("S001")
if salle:
    print(salle.afficher_infos())

# afficher toutes les salles
liste = dao.get_salles()
for s in liste:
    print(s.afficher_infos())

# supprimer
dao.delete_salle("S001")
print("Salle supprimée")