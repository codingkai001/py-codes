import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

# 创建队列，消息持久化
channel.queue_declare(queue='task_queue', durable=True)

message = ''.join(sys.argv[1:]) or 'hello world'
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # 使得消息持久化
    )
)

print("发送： %r" % message)
connection.close()
