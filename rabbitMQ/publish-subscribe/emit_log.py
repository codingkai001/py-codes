import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout',
)
message = ''.join(sys.argv[1:]) or 'Info:hello, world!'
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)
print('发送成功：%r' % message)
connection.close()
