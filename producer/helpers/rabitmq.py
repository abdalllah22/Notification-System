import pika

def send_msg(notification_id):
    
    msg = '{"id": "' + str(notification_id) + '"}'
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='notifications_queue')

    channel.basic_publish(exchange='', routing_key='notifications_queue', body=msg)
    print(" (*******) Notification '" + str(notification_id) + "' is sent to Queue '")
    connection.close()
    
    
        
