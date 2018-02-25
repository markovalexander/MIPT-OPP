import pika
from pymongo import MongoClient

client = MongoClient(host='mongo')

client.drop_database('messages-database')
db = client['messages-database']
db.drop_collection('messages')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='rabbitmq_queue')


def callback(ch, method, properties, body):
	db.messages.save({'message': body.decode()})

channel.basic_consume(callback, queue='rabbitmq_queue', no_ack=True)
channel.start_consuming()
