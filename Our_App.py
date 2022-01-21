import database

# Ajouter Un Contact
database.add_one(5566 ,"Muntaqa" , "Ndiaye" , 774456576 ,"ucncjj@outlook.fr" , "Touba")


#Supprimer un contact
database.delete_one('6')

#Rechercher un contact par son numéro de téléphone
database.phone_lookup(783676587)


#Afficher la liste de tous les contacts
database.show_all()


#Rechercher un contact par son numéro de téléphone
database.update_one('Diop')