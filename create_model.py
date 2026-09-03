import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import os

# Créer le dossier models s'il n'existe pas
os.makedirs('models', exist_ok=True)

# Données factices pour l'entraînement
np.random.seed(42)
n_samples = 100
n_features = 4

# Créer des données aléatoires
X = np.random.rand(n_samples, n_features)
y = np.random.randint(0, 2, n_samples)

# Entraîner un modèle simple
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# Sauvegarder le modèle
joblib.dump(model, 'models/modele.pkl')

print("✅ Modèle créé avec succès dans models/modele.pkl")
print(f"📊 Taille du modèle : {os.path.getsize('models/modele.pkl')} octets")