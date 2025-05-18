

# Liste des actions : nom, prix, bénéfice en % """
# Liste des actions : nom, prix, bénéfice en %
liste_actions = [
    {"nom": "Action-1", "prix": 20, "benefice": 5},
    {"nom": "Action-2", "prix": 30, "benefice": 10},
    {"nom": "Action-3", "prix": 50, "benefice": 15},
    {"nom": "Action-4", "prix": 70, "benefice": 20},
    {"nom": "Action-5", "prix": 60, "benefice": 17},
    {"nom": "Action-6", "prix": 80, "benefice": 25},
    {"nom": "Action-7", "prix": 22, "benefice": 7},
    {"nom": "Action-8", "prix": 26, "benefice": 11},
    {"nom": "Action-9", "prix": 48, "benefice": 13},
    {"nom": "Action-10", "prix": 34, "benefice": 27},
    {"nom": "Action-11", "prix": 42, "benefice": 17},
    {"nom": "Action-12", "prix": 110, "benefice": 9},
    {"nom": "Action-13", "prix": 38, "benefice": 23},
    {"nom": "Action-14", "prix": 14, "benefice": 1},
    {"nom": "Action-15", "prix": 18, "benefice": 3},
    {"nom": "Action-16", "prix": 8, "benefice": 8},
    {"nom": "Action-17", "prix": 4, "benefice": 12},
    {"nom": "Action-18", "prix": 10, "benefice": 14},
    {"nom": "Action-19", "prix": 24, "benefice": 21},
    {"nom": "Action-20", "prix": 114, "benefice": 18},
]

budget_max = 500

def maximiser_profit(actions, budget):
    n = len(actions)
    # tableau[i][b] = bénéfice max avec i premières actions et budget b
    tableau = [[0]*(budget+1) for _ in range(n+1)]

    # Remplissage du tableau
    for i in range(1, n+1):
        prix = actions[i-1]['prix']
        gain = prix * (actions[i-1]['benefice'] / 100)
        for b in range(budget+1):
            if prix <= b:
                tableau[i][b] = max(
                    tableau[i-1][b],
                    tableau[i-1][b - prix] + gain
                )
            else:
                tableau[i][b] = tableau[i-1][b]

    # Reconstruction du portefeuille optimal
    portefeuille = []
    b = budget
    for i in range(n, 0, -1):
        if tableau[i][b] != tableau[i-1][b]:
            action = actions[i-1]
            portefeuille.append(action)
            b -= action['prix']

    portefeuille.reverse()  # Pour garder l'ordre original

    benefice_max = tableau[n][budget]
    return portefeuille, benefice_max

# Exécution
portefeuille_optimal, benefice = maximiser_profit(liste_actions, budget_max)

print("Portefeuille optimal :")
for action in portefeuille_optimal:
    print(f"{action['nom']} - Prix: {action['prix']}€, Bénéfice: {action['benefice']}%")

print(f"\nBénéfice total maximal attendu après 2 ans : {benefice:.2f}€")
print(f"Coût total : {sum(a['prix'] for a in portefeuille_optimal)}€")
print(f"Budget restant : {budget_max - sum(a['prix'] for a in portefeuille_optimal)}€")
