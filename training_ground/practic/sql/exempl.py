import json
import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)

# data = {
#     "name": "Jhon",
#     "marks": {
#         "math": 5,
#         "physic": 10
#     },
#     "last name": "Nemibo"
# }

# r.set("student", json.dumps(data))
data = json.loads(r.get("student"))
print(data)