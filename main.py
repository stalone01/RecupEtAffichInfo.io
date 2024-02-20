def est_majeur(age: int):
    if age <= 0:
        return False
    if age >=18:
        return True
    return False

def recuperer_infos_personne(numero_personne):
    nom_personne = input("Nom de la personne "+str(numero_personne)+":")
    age_personne = input("age de la personne "+str(numero_personne)+":")
    return nom_personne,int(age_personne)

def afficher_infos_personne(numero_personne,nom, age: int):
    print("La personne ",numero_personne,"est", nom, ", Son age est ", age,"ans")
    print("Le nom comporte", len(nom), "lettres")
    if est_majeur(age):
        print("il est majeur")
    else:
        print("il est mineur")


def recuperer_et_afficher_infos_personne(numero_personne):
    nom,age = recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne,nom,age)


nb_personne = 2
for i in range(nb_personne):
    recuperer_et_afficher_infos_personne(i+1)
