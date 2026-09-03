import redis

r = redis.Redis(host="localhost", port=6379)

# écrire la feature d'un client
r.set("client:1234:score_bancaire", 0.71)

print("Feature 'client:1234:score_bancaire' écrite dans Redis.")
