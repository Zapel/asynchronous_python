import redis
import bz2

r = redis.Redis(db=5)
blob = "i have a lot to talk about" * 10000

print(len(blob.encode("utf-8")))

r.set("msg:500", bz2.compress(blob.encode("utf-8")))
print(r.get("msg:500"))
print(len(r.get("msg:500")))
rblob = bz2.decompress(r.get("msg:500")).decode("utf-8")
print(rblob)
print(rblob == blob)

print(r.config_get('databases'))
print(r.info('keyspace') )