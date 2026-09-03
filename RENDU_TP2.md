# RENDU – TP n°2 : De l'automatisation à la plateforme sécurisée

**Module :** MLOps & Déploiement de Modèles
**Formation :** Master 1, Semestre 1 – AI & Big Data
**Établissement :** UAHB – Faculté des Sciences et Techniques, Département STIC
**Enseignant :** Nassour Abdelmahamoud
**Étudiants (binôme) :** Amadou Diallo, Libasse Gassama
**Date de rendu :** ____ / 09 / 2026

---

## Lien du dépôt

🔗 Dépôt GitHub/GitLab : `https://github.com/LibasseGassama/scoring-credit`

---

## Partie 1 – Pipeline CI/CD (Chapitre 6)

**Livrable attendu :** Pipeline visible dans GitLab, toutes les étapes passent au vert.

- [ ] `.gitlab-ci.yml` complété (stages test / scan / build)
- [ ] Pipeline poussé et exécuté sur GitLab
- [ ] Les trois jobs (test, scan, build) passent au vert

**Capture d'écran – pipeline GitLab au vert :**

![Pipeline CI/CD](captures/partie1_cicd.png)

---

## Partie 2 – Déploiement Kubernetes (Chapitre 7)

**Livrable attendu :** Pod à l'état `Running`, API accessible via le Service.

- [ ] `deployment.yaml` complété (Deployment + Service)
- [ ] `kubectl apply -f deployment.yaml` exécuté sans erreur
- [ ] `kubectl get pods` affiche le pod en `Running`
- [ ] API accessible via le Service

**Capture d'écran – `kubectl get pods` et `kubectl get services` :**

![Déploiement Kubernetes](captures/partie2_k8s.png)

---

## Partie 3 – Feature Store Redis (Chapitre 8)

**Livrable attendu :** L'API répond correctement en lisant la feature depuis Redis.

- [ ] Feature écrite dans Redis (`src/ecrire_feature.py`)
- [ ] Lecture de la feature intégrée dans `src/main.py`
- [ ] Requête `/predire` testée avec la feature lue depuis Redis

**Capture d'écran – écriture/lecture Redis et réponse API :**

![Feature Store Redis](captures/partie3_redis.png)

---

## Partie 4 – Monitoring & dérive (Chapitre 9)

**Livrable attendu :** Route `/metrics` accessible et rapport HTML de dérive généré.

- [ ] Route `/metrics` exposée dans `src/main.py`
- [ ] Compteur `predictions_total` incrémenté à chaque appel `/predire`
- [ ] `detecter_derive.py` complété et exécuté
- [ ] `rapport_derive.html` généré

**Capture d'écran – route `/metrics` et rapport de dérive Evidently :**

![Monitoring et dérive](captures/partie4_monitoring.png)

---

## Partie 5 – Sécurisation RBAC (Chapitre 10)

**Livrable attendu :** Le compte restreint ne peut ni créer ni modifier de ressource.

- [ ] `role.yaml` complété (verbes `get`, `list` uniquement)
- [ ] RoleBinding créé (`kubectl create rolebinding ...`)
- [ ] Test de restriction vérifié (ex : `kubectl auth can-i create pods --as=stagiaire`)

**Capture d'écran – RoleBinding créé et test d'accès restreint :**

![RBAC](captures/partie5_rbac.png)

---

## Récapitulatif des livrables finaux

| Livrable | Statut | Preuve |
|---|---|---|
| Pipeline CI/CD (test, scan, build) au vert | ☐ | Partie 1 |
| Déploiement Kubernetes (pod Running, Service actif) | ☐ | Partie 2 |
| Feature Store Redis (écriture + lecture) | ☐ | Partie 3 |
| Monitoring (`/metrics` + rapport de dérive) | ☐ | Partie 4 |
| Accès RBAC restreint vérifié | ☐ | Partie 5 |

---

*Dépôt maintenu public jusqu'à la correction et la réception des notes.*
