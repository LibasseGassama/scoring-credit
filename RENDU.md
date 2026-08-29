# RENDU — TP n°1 : Du prototype au modèle servi

Étudiant : Libasse Gassama & Amadou Diallo
Date : 29-08-2026

## 1. Dépôt Git — Projet structuré, versionné, avec un test qui passe

Capture d'écran du résultat de `poetry run pytest -v` montrant le test au vert.

![test pytest](captures/01_pytest.png)

## 2. Données versionnées — Fichier .dvc pointant vers data/train.csv

Capture d'écran du fichier `data/train.csv.dvc` généré et du commit Git associé.

![dvc add](captures/02_dvc.png)

## 3. Run MLflow — paramètre, métrique et modèle enregistrés

Capture d'écran de l'interface `mlflow ui` (http://localhost:5000) montrant le run avec :
- le paramètre `modele`
- la métrique `precision`
- l'artefact du modèle enregistré

![mlflow ui](captures/03_mlflow.png)

## 4. Image Docker — build et démarrage sans erreur

Capture d'écran du terminal montrant :
- `docker build -t scoring-credit:1.0 .` qui se termine sans erreur
- `docker run -p 8000:8000 scoring-credit:1.0` qui démarre le serveur uvicorn

![docker build/run](captures/04_docker.png)

## 5. API fonctionnelle — endpoint /predire testé

Capture d'écran de la requête `curl` (ou Postman/Swagger `/docs`) et de sa réponse JSON.

![curl predire](captures/05_api.png)

---

Lien du dépôt : https://github.com/LibasseGassama/scoring-credit.git
