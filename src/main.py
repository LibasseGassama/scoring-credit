from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, make_asgi_app
import joblib
import redis

app = FastAPI()
modele = joblib.load("models/modele.pkl")

# Feature Store Redis (Chapitre 8)
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

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

    # Lecture de la feature score_bancaire depuis Redis plutôt que depuis la requête
    score_bancaire = float(r.get(f"client:{donnees.client_id}:score_bancaire"))

    score = modele.predict_proba([[
        donnees.age,
        donnees.revenu,
        donnees.anciennete,
        score_bancaire,
    ]])[0][1]
    return {"score": score, "decision": "accepte" if score > 0.5 else "refuse"}
