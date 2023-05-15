import redis

r = redis.Redis(host='localhost', port=6379, db=0)
#r.set('030194012', '{"prueba":0}')
print(r.get('030194012'))
