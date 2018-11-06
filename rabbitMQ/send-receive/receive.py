import pika


def callback(channel, method, properties, body):
    print(" 收到消息：%s" % body.decode('utf-8'))


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' 等待接收消息。。。')
channel.start_consuming()
