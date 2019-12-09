# Новая вкладка или окно оболочки
import redis
import datetime
import ipaddress

r = redis.Redis(db=5)

# for _ in range(20):
#     r.lpush("ips", "104.174.118.18")
r.lpush("ips", "51.218.112.236")
r.lpush("ips", "90.213.45.98")
r.lpush("ips", "115.215.230.176")
r.lpush("ips", "51.218.112.236")

# Здесь мы размещаем наши вредительские IP адреса
blacklist = set()
MAXVISITS = 15

ipwatcher = redis.Redis(db=5)

while True:
    _, addr = ipwatcher.blpop("ips")
    addr = ipaddress.ip_address(addr.decode("utf-8"))
    now = datetime.datetime.utcnow()
    addrts = f"{addr}:{now.minute}"
    n = ipwatcher.incrby(addrts, 1)
    if n >= MAXVISITS:
        print(f"Hat bot detected!:  {addr}")
        blacklist.add(addr)
    else:
        print(f"{now}:  saw {addr}")
    _ = ipwatcher.expire(addrts, 60)

