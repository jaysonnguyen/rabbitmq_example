import pika, sys, os, time

def main():
    # credentials = pika.PlainCredentials('quinv', 'quinv')
    # parameters = pika.ConnectionParameters(
    #     '34.125.237.190',
    #     5672,
    #     '/',
    #     credentials
    # )
    parameters = pika.URLParameters('amqp://quinv:quinv@localhost:5672/%2F')
    connection = pika.BlockingConnection(parameters)
    # connection = pika.SelectConnection(parameters=parameters)

    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)