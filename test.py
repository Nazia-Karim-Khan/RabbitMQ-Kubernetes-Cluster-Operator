import pika

credentials = pika.PlainCredentials('default_user_046Teogcg7vildAQaEL', 'k4zY2_22wCYmv8mH9fmoUz6fYr1uu5Ky')
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='test_queue')

channel.basic_publish(exchange='', routing_key='test_queue', body='Hello RabbitMQ!')
print("Message sent!")
connection.close()
