from itertools import combinations

# Liste des actions (nom, prix, bénéfice en %)
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

def brute_force_maximiser_profit(actions, budget):
    n = len(actions)
    meilleur_benefice = 0
    meilleur_portefeuille = []

    # Tester toutes les combinaisons possibles (de 1 à n actions)
    for r in range(1, n + 1):
        for subset in combinations(actions, r):
            cout_total = sum(action['prix'] for action in subset)
            if cout_total <= budget:
                benefice_total = sum(
                    action['prix'] * (action['benefice'] / 100)
                    for action in subset
                )
                if benefice_total > meilleur_benefice:
                    meilleur_benefice = benefice_total
                    meilleur_portefeuille = list(subset)

    return meilleur_portefeuille, meilleur_benefice

if __name__ == "__main__":
    portefeuille_optimal, benefice = brute_force_maximiser_profit(liste_actions, budget_max)

    print("Portefeuille optimal (force brute) :")
    for action in portefeuille_optimal:
        print(f"{action['nom']} - Prix: {action['prix']}€, Bénéfice: {action['benefice']}%")

    print(f"\nBénéfice total maximal : {benefice:.2f}€")
    print(f"Coût total : {sum(a['prix'] for a in portefeuille_optimal)}€")
    print(f"Budget restant : {budget_max - sum(a['prix'] for a in portefeuille_optimal)}€")
