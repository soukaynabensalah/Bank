import random
import csv

# Dictionnaires
Clients = {}
Comptes = {}
ClientCompte = {}

def ajouterClient(numCl, MPC, SoldeC):
    numC = genererNumCompte(numCl)
    Clients[numCl] = MPC
    Comptes[numC] = SoldeC
    ClientCompte[numCl] = numC
    print(f"Client {numCl} ajouté avec le compte {numC} et un solde de {SoldeC}.")


def supprimerClient(numC):
    for numCl, compte in ClientCompte.items():
        if compte == numC:
            del Clients[numCl]
            del Comptes[numC]
            del ClientCompte[numCl]
            print(f"Compte {numC} supprimé.")



def modifierMPClient(numCl, ancienMP, nouveauMP):
    if Clients.get(numCl) == ancienMP:
        Clients[numCl] = nouveauMP
        print("Mot de passe modifié avec succès.")
    else:
        print("L'ancien mot de passe est incorrect.")

def deposer(numC, somme):
    if numC in Comptes:
        Comptes[numC] += somme
        print(f"{somme} déposés. Nouveau solde: {Comptes[numC]}")
    else:
        print("Numéro de compte invalide.")

def retirer(numC, somme):
    if numC in Comptes and Comptes[numC] >= somme:
        Comptes[numC] -= somme
        print(f"{somme} retirés. Nouveau solde: {Comptes[numC]}")
    else:
        print("Solde insuffisant ou numéro de compte invalide.")

# Fonction lambda pour générer le numéro de compte
genererNumCompte = lambda numCl: numCl * 100 + random.randint(0, 100)

def ecrirefichierCSV():
    with open("client.csv","w",newline="") as csvfile:
       fieldnames=["numero client","code secret"]
       writer =csv.DictWriter(csvfile, fieldnames=fieldnames)
       writer.writeheader()
       for numCl ,codeSecret in Client.items():
           writer.writerow({"numeroclient":numCl,"codeSecret":codeSecret})

def manipSTS():
    liste = list(ClientCompte.keys())
    tuple_ = tuple(ClientCompte.keys())
    set_ = set(ClientCompte.keys())
    return liste, tuple, set

# Programme principal
def main():
    while True:
        userType = input("Êtes-vous un agent ou un client? (agent/client): ")
        if userType.lower() == 'agent':
            choix = input("1. Ajouter un Compte\n2. Supprimer un Compte\nChoisissez une option: ")
            if choix == '1':
                numCl = int(input("Numéro du client: "))
                MPC = input("Code secret du client: ")
                SoldeC = float(input("Solde initial du compte: "))
                ajouterClient(numCl, MPC, SoldeC)
            elif choix == '2':
                numC = int(input("Numéro du compte à supprimer: "))
                supprimerClient(numC)
            elif userType.lower() == 'client':
                numCl = int(input("Numéro du client: "))
                choix = input("1. Modifier son mot de passe\n2. Afficher son solde\n3. Déposer une somme d'argent\n4. Retirer une somme d'argent\nChoisissez une option: ")
                if choix == '1':
                    ancienMP = input("Ancien mot de passe: ")
                    nouveauMP = input("Nouveau mot de passe: ")
                    modifierMPClient(numCl, ancienMP, nouveauMP)
                elif choix == '2':
                    numC = ClientCompte(numCl)
                    if numC:
                        print(f"Votre solde est de {Comptes[numC]}")
                    else:
                        print("Compte introuvable.")
                elif choix == '3':
                    numC = ClientCompte.get(numCl)
                    somme = float(input("Somme à déposer: "))
                    deposer(numC, somme)
                elif choix == '4':
                    numC = ClientCompte.get(numCl)
                    somme = float(input("Somme à retirer: "))
                    retirer(numC, somme)
                else:
                    print("Type d'utilisateur non reconnu.")
continuer = input("Voulez-vous continuer? (oui/non): ")
if continuer.lower() != 'oui':
break

if __name__ == "__main__":
main()
