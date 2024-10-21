import json
from stats_functions import *


# Charge les entreprises à partir du fichier JSON
with open('data/employes_data_test.json', 'r') as f:
    enterprises = json.load(f)

for enterprise in enterprises.keys():
    employees = enterprises[enterprise]

    print(f"Filiale: {enterprise}\n")

    # Calcul des salaires mensuels
    results = calculate_monthly_salary(employees)

    # Tri des employés par salaire mensuel décroissant
    results = sorted(results, key=lambda x: x[2], reverse=True)

    # Affichage des salaires
    for name, job, salary in results:
        print(f"{name:<10} | {job:<15} | Salaire mensuel: {salary:.2f}€")

    print()
    print('=' * 60, '\n')

    # Ajout des salaires aux employés pour calculer les statistiques
    for i, employee in enumerate(employees):
        employees[i]['salary'] = results[i][2]  # On récupère le salaire calculé précédemment

    # Calcul et affichage des statistiques
    stats = salary_statistics(employees)
    print(f"Statistiques des salaires pour la filiale {enterprise}:")
    print(f"Salaire moyen: {stats['average_salary']:.2f}€")
    print(f"Salaire le plus élevé: {stats['max_salary']:.2f}€")
    print(f"Salaire le plus bas: {stats['min_salary']:.2f}€")
    print()
    print('=' * 60, '\n')