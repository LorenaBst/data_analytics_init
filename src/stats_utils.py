import pandas as pd

def analyser_ventes(transactions) : 
    montants = pd.Series(transactions)  #creation d'une serie pandas
    montants_valides = montants[montants > 0]   #nettoyage
    nombre = len(montants_valides)  #stats
    somme = float(montants_valides.sum())
    moyenne = float(montants_valides.mean())
    mediane = float(montants_valides.median())
    ecart_type = float(montants_valides.std())
    maxi = float(montants_valides.max())
    mini = float(montants_valides.min())
    anomalies = montants_valides[montants_valides > (2* moyenne)].tolist()
    return {
        "Nombre_transactions": nombre,
        "somme" : somme, 
        "moyenne" : moyenne, 
        "mediane" : mediane, 
        "ecart_type" : ecart_type,
        "valeur_maxi" : maxi,
        "valeur_mini" : mini,
        "anomalies" : anomalies,
    }


ventes = [200, 300, -90, 0, -10, 40, 10000]

stats_ventes = analyser_ventes(ventes)
print(stats_ventes)






