def calculate_monthly_salary(employees: list[dict]) -> list[tuple]:
    """
    Calcule le salaire mensuel des employés, en prenant en compte les heures supplémentaires.

    Paramètres :
    - employees (list[dict]) : Liste de dictionnaires contenant les informations des employés. Chaque dictionnaire
      doit inclure les clés suivantes :
        - 'name' (str) : Le nom de l'employé.
        - 'job' (str) : Le poste de l'employé.
        - 'hourly_rate' (float) : Le taux horaire de l'employé.
        - 'weekly_hours_worked' (float) : Le nombre d'heures travaillées par semaine.
        - 'contract_hours' (float) : Le nombre d'heures contractuelles hebdomadaires (sans heures supplémentaires).

    Retourne :
    - list[tuple] : Liste de tuples, où chaque tuple contient le nom, le poste et le salaire mensuel calculé pour 
      chaque employé.
    """
    OVERTIME_RATE = 1.5  # Taux pour les heures supplémentaires
    results = []

    for employee in employees:
        name = employee['name']
        job = employee['job']
        hourly_rate = employee['hourly_rate']
        weekly_hours_worked = employee['weekly_hours_worked']
        contract_hours = employee['contract_hours']

        # Calcul du salaire hebdomadaire avec gestion des heures supplémentaires
        if weekly_hours_worked > contract_hours:
            overtime_hours = weekly_hours_worked - contract_hours
            weekly_salary = (contract_hours * hourly_rate) + (overtime_hours * hourly_rate * OVERTIME_RATE)
            
        # Si l'employé a fait moins d'heures que son contrat
        elif weekly_hours_worked < contract_hours:
            weekly_salary = contract_hours * hourly_rate

        else:
            weekly_salary = weekly_hours_worked * hourly_rate

        # Calcul du salaire mensuel (4 semaines)
        monthly_salary = weekly_salary * 4
        results.append((name, job, monthly_salary))

    return results


def salary_statistics(employees: list[dict]) -> dict:
    """
    Calcule les statistiques sur les salaires des employés : salaire moyen, salaire le plus élevé et salaire le plus bas.

    Paramètres :
    - employees (list[dict]) : Liste de dictionnaires contenant les informations des employés. Chaque dictionnaire 
      doit inclure la clé 'salary' (float), représentant le salaire de chaque employé.

    Retourne :
    - dict : Dictionnaire contenant les statistiques suivantes :
        - 'average_salary' (float) : Salaire moyen des employés.
        - 'max_salary' (float) : Salaire le plus élevé.
        - 'min_salary' (float) : Salaire le plus bas.
    """
    salaries = [employee['salary'] for employee in employees]

    # Moyenne des salaires
    average_salary = sum(salaries) / len(salaries) if salaries else 0.0

    # Salaire le plus élevé
    max_salary = max(salaries) if salaries else 0.0

    # Salaire le plus bas
    min_salary = min(salaries) if salaries else 0.0

    return {
        'average_salary': average_salary,
        'max_salary': max_salary,
        'min_salary': min_salary
    }