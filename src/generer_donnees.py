from sklearn.datasets import make_classification
import pandas as pd
import os


def generer_donnees():
    X, y = make_classification(n_samples=500, n_features=4, random_state=42)
    df = pd.DataFrame(X, columns=["age", "revenu", "anciennete", "score_bancaire"])
    df["decision"] = y
    return df


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    generer_donnees().to_csv("data/train.csv", index=False)
    print("Fichier data/train.csv généré avec succès !")
