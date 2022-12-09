import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('34.125.237.190'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print("[x] Sent 'Hello World!'")

connection.close()