import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# données de référence = données d'entraînement du TP1
reference_data = pd.read_csv("data/train.csv")

# données récentes = à remplacer par un extrait de trafic réel de l'API
current_data = pd.read_csv("data/train.csv").sample(frac=0.3, random_state=1)

rapport = Report(metrics=[DataDriftPreset()])
rapport.run(reference_data=reference_data, current_data=current_data)
rapport.save_html("rapport_derive.html")

print("Rapport de dérive généré : rapport_derive.html")
