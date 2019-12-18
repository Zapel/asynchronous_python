import redis
import json
from cryptography.fernet import Fernet

r = redis.Redis(db=4)

cipher = Fernet(Fernet.generate_key())

info = {"cardnum": 2211849528391929,
        "exp": [2020, 9],
        "cv2": 842}

r.set("user:1000", cipher.encrypt(json.dumps(info).encode("utf-8")))

print(r.get("user:1000"))
print(cipher.decrypt(r.get("user:1000")))
print(json.loads(cipher.decrypt(r.get("user:1000"))))