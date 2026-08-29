from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
modele = joblib.load("models/modele.pkl")


class DonneesClient(BaseModel):
    age: float
    revenu: float
    anciennete: float
    score_bancaire: float


@app.post("/predire")
def predire(donnees: DonneesClient):
    score = modele.predict_proba([[
        donnees.age,
        donnees.revenu,
        donnees.anciennete,
        donnees.score_bancaire,
    ]])[0][1]
    return {"score": score, "decision": "accepte" if score > 0.5 else "refuse"}
