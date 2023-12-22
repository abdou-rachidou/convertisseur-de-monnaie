from forex_python.converter import CurrencyRates
import json
import sys

c = CurrencyRates()
historique = []


print("\n")
print("Bonjour et Bienvenue dans mon programme de conversion.")


def menu():
    print("1. Faire une nouvelle conversion")
    print("2. Afficher l'Historique")
    print("3. Afficher la liste des devises")
    print("4. Ajouter une nouvelle devise")
    print("5. Quitter le programme")


def activate_menu():
    global historique, devises_pays
    # Chargement des devises depuis le fichier
    devises_pays = load_devises_from_file()
    menu()
    print("\n")
    user = input("Veuillez choisir un nombre (1-5) : ")
    if user == '1':
        convertisseur()
    elif user == '2':
        historique = load_file()
        print(historique)
    elif user == '3':
        afficher_liste_devises()
    elif user == '4':
        ajouter_nouvelle_devise()
    elif user == '5':
        print("Fin du programme, Au revoir !")
        sys.exit()  # Terminer le programme


def load_devises_from_file(filename="devises.json"):
    try:
        with open(filename, 'r') as file:
            devises_pays = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        devises_pays = {}

    return devises_pays

# Chargement des devises depuis le fichier
devises_pays = load_devises_from_file()



def save_devises_to_file(devises_pays, filename="devises.json"):
    with open(filename, 'w') as file:
        json.dump(devises_pays, file, indent=4)


def afficher_liste_devises():
    global devises_pays
    print("Liste des devises et de leurs pays correspondants :")
    for devise, pays in devises_pays.items():
        print(f"{devise} : {pays}")



def ajouter_nouvelle_devise():
    global devises_pays
    nouvelle_devise = input("Veuillez entrer le code de la nouvelle devise (ex: USD) : ").upper()
    nouveau_pays = input("Veuillez entrer le pays correspondant à la nouvelle devise : ")
    devises_pays[nouvelle_devise] = nouveau_pays
    save_devises_to_file(devises_pays)
    print(f"La nouvelle devise ({nouvelle_devise}) a été ajoutée avec succès.")


def load_file(filename="historique.txt"):
    try:
        with open(filename, 'r') as file:
            historique = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        historique = []

    return historique

def save_file(historique, filename="historique.txt"):
    with open(filename, 'w') as file:
        json.dump(historique, file, indent=4)

def convertisseur():
    global historique
    while True: 
        devise_origine = input("Veuillez entrer la devise initiale (ex : USD...) : ").upper()
        devise_destination = input("Veuillez entrer la devise de destination (ex : EUR) : ").upper()

        while True:
            try:
                montant = float(input("Veuillez entrer la valeur que vous souhaitez convertir : "))
                if montant < 0:
                    print("Le montant doit être supérieur à zéro")
                else:
                    break
            except ValueError:
                print("La conversion n'est pas possible")

        print(montant, devise_origine, "en", devise_destination)
        resultat = c.convert(devise_origine, devise_destination, montant)
        print(resultat, devise_destination)

        # Enregistrement de la conversion dans l'historique
        save_option = input("Voulez-vous enregistrer votre conversion dans l'historique? (Oui/Non) : ").lower()
        if save_option == 'oui':
            conversion_entry = {
                "Devises": f"{devise_origine} en {devise_destination}",
                "montant": f"{montant} {devise_origine}",
                "resultat": f"{resultat} {devise_destination}"
            }

            historique.append(conversion_entry)
            save_file(historique)
            print("La conversion a été enregistrée avec succès")

        # Possibilité de refaire une autre conversion
        user_choice = input("Voulez-vous refaire une autre conversion ? (Oui/Non) : ").lower()
        if user_choice != 'oui':
            print("\n")
            break  # Sortir de la boucle interne pour revenir au menu principal

# La boucle infinie pour revenir au menu principal après chaque conversion
while True:
    activate_menu()
