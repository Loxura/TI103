#prints menu with options
def afficher_menu():
    print("\nMenu :")
    print("1. Filtrer les données météo par ville")
    print("2. Filtrer les données météo par ville et période")
    print("3. Déterminer la température maximale et minimale d'une ville")
    print("4. Déterminer la température moyenne d'une ville")
    print("5. Quitter")

#filters by cities
def filtrer_par_ville(donnees, ville):
    ville_lower = ville.lower()
    resultat = [donnee for donnee in donnees if donnee[1].lower() == ville_lower]
    for donnee in resultat:
        print(donnee)

#filters by city and timestamp
def filtrer_par_ville_et_periode(donnees, ville, debut, fin):
    ville_lower = ville.lower()
    resultat = [donnee for donnee in donnees if donnee[1].lower() == ville_lower and debut <= donnee[0] <= fin]
    if resultat:
        for donnee in resultat:
            print(donnee)
    else:
        print('\n')
        print(f"Pas de données pour {ville} entre {debut} et {fin}. Verifiez que la ville et les dates sont correctes !")

#filters by temperatures
def determiner_temperature_extreme(donnees, ville):
    ville_lower = ville.lower()
    temperatures = [int(donnee[2]) for donnee in donnees if donnee[1].lower() == ville_lower]
    if temperatures:
        print(f"Température maximale à {ville} : {max(temperatures)}")
        print(f"Température minimale à {ville} : {min(temperatures)}")
    else:
        print(f"Aucune donnée pour la ville de {ville}")

#calculates avg temperature
def determiner_temperature_moyenne(donnees, ville):
    ville_lower = ville.lower()
    temperatures = [int(donnee[2]) for donnee in donnees if donnee[1].lower() == ville_lower]
    if temperatures:
        moyenne = sum(temperatures) / len(temperatures)
        print(f"Température moyenne à {ville} : {moyenne}")
    else:
        print(f"Aucune donnée pour la ville de {ville}")


#main app
if __name__ == "__main__":

    #data 
    donnees_meteo = [
        ['2024-01-01', 'Toronto', 5, -2, 10],
        ['2024-01-02', 'Toronto', 6, -3, 12],
        ['2024-01-03', 'Toronto', 4, -1, 8],
        ['2024-01-04', 'Toronto', 3, -4, 6],
        ['2024-01-05', 'Toronto', 2, -2, 7],
        ['2024-01-06', 'Toronto', 1, -3, 5],
        ['2024-01-07', 'Toronto', 0, -5, 4],
        ['2024-01-08', 'Toronto', -1, -6, 3],
        ['2024-01-09', 'Toronto', -2, -7, 2],
        ['2024-01-10', 'Toronto', -3, -8, 1],
        ['2024-01-01', 'Montreal', 3, -1, 6],
        ['2024-01-02', 'Montreal', 2, -2, 5],
        ['2024-01-03', 'Montreal', 1, -3, 4],
        ['2024-01-04', 'Montreal', 0, -4, 3],
        ['2024-01-05', 'Montreal', -1, -5, 2],
        ['2024-01-06', 'Montreal', -2, -6, 1],
        ['2024-01-07', 'Montreal', -3, -7, 0],
        ['2024-01-08', 'Montreal', -4, -8, -1],
        ['2024-01-09', 'Montreal', -5, -9, -2],
        ['2024-01-10', 'Montreal', -6, -10, -3],
        ['2024-01-01', 'Vancouver', 10, 5, 15],
        ['2024-01-02', 'Vancouver', 11, 4, 16],
        ['2024-01-03', 'Vancouver', 9, 6, 14],
        ['2024-01-04', 'Vancouver', 8, 5, 13],
        ['2024-01-05', 'Vancouver', 7, 4, 12],
        ['2024-01-06', 'Vancouver', 6, 3, 11],
        ['2024-01-07', 'Vancouver', 5, 2, 10],
        ['2024-01-08', 'Vancouver', 4, 1, 9],
        ['2024-01-09', 'Vancouver', 3, 0, 8],
        ['2024-01-10', 'Vancouver', 2, -1, 7],
        ['2024-01-01', 'Calgary', -5, -10, -2],
        ['2024-01-02', 'Calgary', -6, -11, -3],
        ['2024-01-03', 'Calgary', -7, -12, -4],
        ['2024-01-04', 'Calgary', -8, -13, -5],
        ['2024-01-05', 'Calgary', -9, -14, -6],
        ['2024-01-06', 'Calgary', -10, -15, -7],
        ['2024-01-07', 'Calgary', -11, -16, -8],
        ['2024-01-08', 'Calgary', -12, -17, -9],
        ['2024-01-09', 'Calgary', -13, -18, -10],
        ['2024-01-10', 'Calgary', -14, -19, -11],
        
        ['2024-01-01', 'Ottawa', -2, -7, 1],
        ['2024-01-02', 'Ottawa', -1, -6, 2],
        ['2024-01-03', 'Ottawa', 0, -8, 3],
        ['2024-01-04', 'Ottawa', -1, -10, -3],
        ['2024-01-05', 'Ottawa', -3, -12, 0],
        ['2024-01-06', 'Ottawa', -5, -15, -2],
        ['2024-01-07', 'Ottawa', -6, -17, -3],
        ['2024-01-08', 'Ottawa', -8, -20, -5],
        ['2024-01-09', 'Ottawa', -10, -22, -7],
        ['2024-01-10', 'Ottawa', -12, -25, -8],

        ['2024-01-01', 'Edmonton', -8, -16, -2],
        ['2024-01-02', 'Edmonton', -7, -14, -1],
        ['2024-01-03', 'Edmonton', -6, -13, 0],
        ['2024-01-04', 'Edmonton', -5, -12, 1],
        ['2024-01-05', 'Edmonton', -4, -10, 2],
        ['2024-01-06', 'Edmonton', -8, -15, -3],
        ['2024-01-07', 'Edmonton', -10, -18, -5],
        ['2024-01-08', 'Edmonton', -12, -20, -6],
        ['2024-01-09', 'Edmonton', -14, -22, -8],
        ['2024-01-10', 'Edmonton', -15, -25, -10],

        ['2024-01-01', 'Winnipeg', -12, -20, -8],
        ['2024-01-02', 'Winnipeg', -10, -18, -6],
        ['2024-01-03', 'Winnipeg', -8, -16, -4],
        ['2024-01-04', 'Winnipeg', -15, -22, -10],
        ['2024-01-05', 'Winnipeg', -14, -21, -9],
        ['2024-01-06', 'Winnipeg', -13, -19, -7],
        ['2024-01-07', 'Winnipeg', -11, -17, -5],
        ['2024-01-08', 'Winnipeg', -9, -15, -3],
        ['2024-01-09', 'Winnipeg', -7, -14, -2],
        ['2024-01-10', 'Winnipeg', -6, -12, -1]]

    while True:
        afficher_menu()
        choix = input("Choix : ")
        if choix == "1":
            ville = input("Ville : ")
            filtrer_par_ville(donnees_meteo, ville)
        elif choix == "2":
            ville = input("Ville : ")
            debut = input("Date de début (YYYY-MM-DD) : ")
            fin = input("Date de fin (YYYY-MM-DD) : ")
            filtrer_par_ville_et_periode(donnees_meteo, ville, debut, fin)
        elif choix == "3":
            ville = input("Ville : ")
            determiner_temperature_extreme(donnees_meteo, ville)
        elif choix == "4":
            ville = input("Ville : ")
            determiner_temperature_moyenne(donnees_meteo, ville)
        elif choix == "5":
            print("Fin du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
