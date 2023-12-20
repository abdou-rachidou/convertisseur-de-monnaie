from forex_python.converter import CurrencyRates

c = CurrencyRates()
RUNNING = True

print("\n")
def convertisseur():
    devise_origine = input("Veuillez entrer la devise initiale (ex : USD...) : ").upper()
    devise_destination = input("Veuillez entrer la devise de destination (ex : euro) : ").upper()

    while RUNNING :
        try:
            montant = float(input("Veuillez entrer la valeur que vous souhaitez convertir : "))
        except ValueError:
            print("La valeur entrer n'est pas valide")
            continue
        
        if montant < 0:
            print("Le montant doit être supérieur à zéro")
            continue
        else :
            break

    print(montant, devise_origine, "en", devise_destination)
    resultat = c.convert(devise_origine, devise_destination, montant)
    print(resultat, devise_destination)
convertisseur()