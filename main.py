from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# ajouter
s1 = Salle("S002", "Salle bureautique", "Bureau", 10)
ok, msg = service.ajouter_salle(s1)
print(msg)

# afficher
for s in service.recuperer_salles():
    print(s.afficher_infos())

# rechercher
s = service.rechercher_salle("S002")
if s:
    print("Trouvée :", s.afficher_infos())

# modifier
s2 = Salle("S002", "Salle bureautique modifiee", "Bureau", 15)
ok, msg = service.modifier_salle(s2)
print(msg)

# supprimer
service.supprimer_salle("S002")
print("Salle supprimée")