import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='rabbitmq_queue')

for line in sys.stdin:
	channel.basic_publish(exchange='',
						  routing_key='rabbitmq_queue',
						  body=line)

connection.close()
