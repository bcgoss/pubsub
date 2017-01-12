import redis
import time

#deprecated, Use publish.rb
r = redis.StrictRedis()
listeners = r.publish('my-channel', 'hello world')
while listeners == 0:
  listeners = r.publish('my-channel', 'hello world')
  print listeners
  time.sleep(1)

print 'Complete'
