import redis
from datetime import timedelta


r = redis.Redis(db=2)
r.setex("runner", timedelta(minutes=1), value="now you see me, now you don't")
# r.bgsave()
print(r.ttl("runner"))
print(r.pttl("runner"))
print(r.get("runner"))

r.expire("runner", timedelta(seconds=3))

print(r.get("runner"))
print(r.exists("runner"))