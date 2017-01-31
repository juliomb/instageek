from django.core.management.base import BaseCommand
import pika
import json

from django.utils.encoding import smart_text


class Command(BaseCommand):
    help = 'Runs an events receiver'

    @staticmethod
    def callback(ch, method, properties, body):
        event_data = json.loads(smart_text(body))
        if event_data.get('type') == 'following':
            print(" [x] User {0} now folows user {1}".format(event_data.get('origin'), event_data.get('target')))

    def handle(self, *args, **options):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='events', type='fanout')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        channel.queue_bind(exchange='events', queue=queue_name)
        print(' [*] Waiting for logs. To exit press CTRL+C')
        channel.basic_consume(self.callback, queue=queue_name)
        channel.start_consuming()
