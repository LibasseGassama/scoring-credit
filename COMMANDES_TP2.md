# Commandes du TP n°2 — De l'automatisation à la plateforme sécurisée

## Partie 1 — CI/CD (GitHub Actions)

Le pipeline est dans `.github/workflows/ci.yml`. Il se déclenche automatiquement à chaque `git push`.

```powershell
git add .
git commit -m "Ajout pipeline CI/CD, Redis, monitoring, K8s, RBAC"
git push
```

Puis va sur GitHub → onglet **Actions** pour voir le pipeline s'exécuter.

## Partie 2 — Kubernetes

Prérequis : Minikube (ou k3s) démarré, `kubectl` configuré.

```powershell
minikube start
```

Construis l'image Docker puis charge-la dans Minikube (car Minikube a son propre environnement Docker isolé) :

```powershell
docker build -t scoring-credit:1.0 .
minikube image load scoring-credit:1.0
```

Déploie :

```powershell
kubectl apply -f k8s/deployment.yaml
kubectl get pods
kubectl get services
```

Le pod doit passer à l'état `Running`. Pour tester l'API depuis l'extérieur du cluster :

```powershell
minikube service api-scoring
```

## Partie 3 — Feature Store Redis

Lance un conteneur Redis local :

```powershell
docker run -d -p 6379:6379 --name redis-local redis:7-alpine
```

Installe la dépendance Python et écris la feature :

```powershell
poetry add redis
poetry run python -m src.ecrire_feature
```

Relance l'API (`uvicorn` ou le conteneur Docker), puis teste `/predire` : le champ `score_bancaire` est désormais lu depuis Redis plutôt qu'envoyé dans la requête.

```powershell
poetry run uvicorn src.main:app --reload
```

Exemple de requête (le schéma attend maintenant `age`, `revenu`, `anciennete`, `client_id`) :

```json
{
  "age": 35,
  "revenu": 2500,
  "anciennete": 24,
  "client_id": "1234"
}
```

## Partie 4 — Monitoring (Prometheus + Evidently)

Installe les dépendances :

```powershell
poetry add prometheus-client evidently
```

Vérifie la route `/metrics` dans le navigateur, une fois l'API lancée :

```
http://localhost:8000/metrics
```

Envoie quelques requêtes sur `/predire`, puis rafraîchis `/metrics` : le compteur `predictions_total` doit augmenter.

Génère le rapport de dérive :

```powershell
poetry run python detecter_derive.py
```

Ouvre `rapport_derive.html` dans un navigateur.

## Partie 5 — RBAC (accès restreint)

```powershell
kubectl apply -f k8s/role.yaml
kubectl create rolebinding lecture --role=lecture-seule --user=stagiaire
```

Vérifie que la restriction fonctionne (doit répondre `no`) :

```powershell
kubectl auth can-i create pods --as=stagiaire
kubectl auth can-i get pods --as=stagiaire
```

Le premier doit refuser (`no`), le second doit autoriser (`yes`) — preuve que l'accès est bien restreint à la lecture seule.
