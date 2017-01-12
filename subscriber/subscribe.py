import redis
import time
import json

class Subscriber:
    def __init_(self):
        r = redis.StrictRedis()

        p = r.pubsub()
        p.subscribe('my-channel')

    def message_received(message, attempts):
      too_many = attempts > 5
      null = message is None

      if too_many:
        return True
      elif not null:
        return message['type'] == 'message'
      else:
        return False

    def make_email(url):

      document = """<!DOCTYPE html>
        <html>
          <head>
            <meta content='text/html; charset=UTF-8' http-equiv='Content-Type' />
          </head>
          <body>
            <h1>You have been invited to create a Census Account</h1>
            <p>Census is the Turing School of Software Design's identity management application.</p>
            <button type='button' name='button'><a href='"""+url+"""'>Register</h></button>
            <p>Thanks for joining!</p>
          </body>
        </html>"""
      return document

    def listen:
        message = p.get_message()
        attempts = 0
        while not message_received(message, attempts):
          message = p.get_message()
          attempts+= 1
          time.sleep(0.5)
        if message is None:
            print 'No message received, timing out'
        else:
            data = json.loads(message['data'])
            print make_email(data['url'])
