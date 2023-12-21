from forex_python.converter import CurrencyRates
import json
import sys

c = CurrencyRates()
historique = []

print("\n")
print("Bonjour et Bienvenue dans mon programme de conversion.")

def menu():
    print("1. Faire une nouvelle convertion")
    print("2. Afficher l'Historique")
    print("3. Quitter le programme")

def activate_menu():
    global historique 
    menu()
    print("\n")
    user = input("Veuillez choisir un nombre (1-3) : ")
    if user == '1':
        convertisseur()
    elif user == '2':
        historique = load_file()
        print(historique)
    elif user == '3':
        print("Fin du programme, Au revoir !")
        sys.exit()  # Terminer le programme

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
