from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_client import Counter, make_asgi_app
import joblib
import redis

app = FastAPI()
modele = joblib.load("models/modele.pkl")

# --- Partie 3 : Feature Store Redis ---
r = redis.Redis(host="localhost", port=6379)

# --- Partie 4 : Monitoring Prometheus ---
app.mount("/metrics", make_asgi_app())
compteur = Counter("predictions_total", "Nombre de prédictions")


class DonneesClient(BaseModel):
    age: float
    revenu: float
    anciennete: float
    score_bancaire: float


@app.post("/predire")
def predire(donnees: DonneesClient):
    compteur.inc()

    # lecture de la feature stockée dans Redis avant la prédiction
    score_bancaire = float(r.get("client:1234:score_bancaire"))

    score = modele.predict_proba([[
        donnees.age,
        donnees.revenu,
        donnees.anciennete,
        score_bancaire,
    ]])[0][1]
    return {"score": score, "decision": "accepte" if score > 0.5 else "refuse"}
