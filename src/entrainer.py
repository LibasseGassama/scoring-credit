import os
import joblib
import mlflow
from sklearn.linear_model import LogisticRegression
from src.generer_donnees import generer_donnees

df = generer_donnees()
X, y = df.drop(columns=["decision"]), df["decision"]

with mlflow.start_run():
    mlflow.log_param("modele", "regression_logistique")
    modele = LogisticRegression().fit(X, y)
    precision = modele.score(X, y)
    mlflow.log_metric("precision", precision)
    mlflow.sklearn.log_model(modele, "modele")

    os.makedirs("models", exist_ok=True)
    joblib.dump(modele, "models/modele.pkl")
    print(f"Modèle entraîné, précision = {precision:.3f}")
    print("Modèle sauvegardé dans models/modele.pkl")
