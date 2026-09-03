import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# reference_data = données d'entraînement, current_data = données récentes
reference = pd.read_csv("data/train.csv").drop(columns=["decision"])
current = pd.read_csv("data/train.csv").drop(columns=["decision"])  # à remplacer par de vraies données récentes

rapport = Report(metrics=[DataDriftPreset()])
rapport.run(reference_data=reference, current_data=current)
rapport.save_html("rapport_derive.html")
print("Rapport de dérive généré : rapport_derive.html")
