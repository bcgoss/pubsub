require 'redis'
class Publisher

  def initialize(list)
    list.each {|invitation| do send(invitation.address, invitation.url)}
  end

  def message_sent?(attempts, listeners)
    attempts > 5 || listeners > 0
  end

  def send(adress, url)
    r = Redis.new
    data = {address: address, url: url}.to_json

    listeners = r.publish('my-channel', 'hello world')
    attempts = 0
    until message_sent?(attempts, listeners) do
      listeners = r.publish('my-channel', 'hello world')
      attempts+=1
      sleep(1)
    end
  end
end
