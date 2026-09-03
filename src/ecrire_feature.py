import redis

# Se connecter à Redis sur localhost (depuis votre machine)
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Écrire la feature
r.set("client:1234:score_bancaire", 0.71)
print("✅ Feature écrite : client:1234:score_bancaire = 0.71")

# Vérifier
value = r.get("client:1234:score_bancaire")
print(f"✅ Lecture : {value}")
