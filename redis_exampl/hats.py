import redis
import random
import logging

class OutOfStockError(Exception):
    """Используется, когда на PyHats заканчивается самый популярный товар"""

random.seed(444)
hats = {f"hat:{random.getrandbits(32)}": i for i in (
    {
        "color": "black",
        "price": 49.99,
        "style": "fitted",
        "quantity": 1000,
        "npurchased": 0,
    },
    {
        "color": "maroon",
        "price": 59.99,
        "style": "hipster",
        "quantity": 500,
        "npurchased": 0,
    },
    {
        "color": "green",
        "price": 99.99,
        "style": "baseball",
        "quantity": 200,
        "npurchased": 0,
    })
        }

def buyitem(r: redis.Redis, itemid: int) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                # Получение доступного инвентаря, поиск изменений
                # связанных с ID объекта перед транзакцией
                pipe.watch(itemid)
                nleft: bytes = r.hget(itemid, "quantity")
                if nleft > b"0":
                    pipe.multi()
                    pipe.hincrby(itemid, "quantity", -1)
                    pipe.hincrby(itemid, "npurchased", 1)
                    pipe.execute()
                    break
                else:
                    # Остановка поиска ID объекта
                    pipe.unwatch()
                    raise OutOfStockError(
                        f"Sorry, {itemid} is out of stock!"
                    )
            except redis.WatchError:
                # Регистрация общего количества ошибок данного пользователя,
                # с последующей попыткой повторения процесса WATCH/HGET/MULTI/EXEC
                error_count += 1
                logging.warning(
                    "WatchError #%d: %s; retrying",
                    error_count, itemid
                )
    return None

r = redis.Redis(db=1)

with r.pipeline() as pipe:
    for h_id, hat in hats.items():
        pipe.hmset(h_id, hat)
    pipe.execute()
r.bgsave()

# print(r.hincrby("hat:56854717", "quantity", -1))
# print(r.hget("hat:56854717", "quantity"))
# print(r.hincrby("hat:56854717", "npurchased", 1))
print(r.keys())


# print(buyitem(r, "hat:56854717"))
# print(r.hmget("hat:56854717", "quantity", "npurchased"))

for _ in range(201):
    print(buyitem(r, "hat:56854717"))
    print(r.hmget("hat:56854717", "quantity", "npurchased"))















