import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('等待接收消息。。。')


def callback(ch, method, properties, body):
    print(" 接收 %r" % body)
    time.sleep(body.count(b'.'))
    print("完成。。。")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 每次给worker分配一个任务，确认完成时再次分配第二个任务
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
