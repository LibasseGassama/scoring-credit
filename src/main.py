from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, make_asgi_app
import joblib
import redis

app = FastAPI()
modele = joblib.load("models/modele.pkl")

# Feature Store Redis (Chapitre 8)
r = redis.Redis(host="redis-service", port=6379, decode_responses=True)

# Monitoring Prometheus (Chapitre 9)
app.mount("/metrics", make_asgi_app())
compteur = Counter("predictions_total", "Nombre de prédictions")


class DonneesClient(BaseModel):
    age: float
    revenu: float
    anciennete: float
    client_id: str = "1234"


@app.post("/predire")
def predire(donnees: DonneesClient):
    compteur.inc()
    # Récupérer le score bancaire depuis Redis
    score_bancaire = r.get(f"client:{donnees.client_id}:score_bancaire")
    
    # Si la feature n'existe pas, utiliser une valeur par défaut
    if score_bancaire is None:
        score_bancaire = 0.5
        print(f"⚠️ Feature manquante pour client {donnees.client_id}, utilisation de 0.5")
    else:
        score_bancaire = float(score_bancaire)
    
    # Créer le tableau de features
    features = [[
        donnees.age,
        donnees.revenu,
        donnees.anciennete,
        score_bancaire
    ]]
    
    # Prédiction
    proba = modele.predict_proba(features)[0][1]
    prediction = 1 if proba > 0.5 else 0
    
    return {
        "client_id": donnees.client_id,
        "prediction": prediction,
        "probabilite": float(proba),
        "score_bancaire": score_bancaire
    }