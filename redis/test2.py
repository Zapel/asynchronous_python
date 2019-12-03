import redis

# class Redis(object):
#     def __init__(self, host='localhost', port=6379, db=0, password=None, socket_timeout=None):
#
#     def print_str(self):
#         print('Hello')





r = redis.Redis
r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"})

print(r.get("Bahamas"))