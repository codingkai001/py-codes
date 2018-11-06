import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while True:
    message = input(">>>请输入发送的消息(输入quit停止发送进程)：")
    if message != 'quit':
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body=message
        )
        print('发送成功。。。')
    else:
        break
connection.close()
