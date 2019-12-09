import redis

r = redis.StrictRedis(host='localhost', port=6379, db=1)

#присваиваем переменной test1 значение 5
r.set('test1', 5)

#получаем из переменной test1 значение
r.get('test1')
print(r.get('test1'))

#уменьшаем значение test1 на 2 (если значение является int)
r.decr('test1', 2) # выдаст 3

#увеличивает значение test1 на 2 (если значение является int)
r.incr('test1', 2) # выдаст 5

#переменная test1 будет удалена через 30 секунд
r.expire('test1', 30)

#переменная test1 будет удалена
r.delete('test1')

#сохранить все данные в памяти на диск
r.bgsave()

#очистить всю выбраную базу
r.flushdb()

r.config_get('databases')