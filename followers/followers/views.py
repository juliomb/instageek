import pika
import json

from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from followers.models import Relationship
from followers.serializers import RelationshipSerializer




class FollowViewSet(CreateModelMixin, GenericViewSet):

    serializer_class = RelationshipSerializer
    queryset = Relationship.objects.all()

    def perform_create(self, serializer):
        serializer.save(origin=self.request.user.pk)

        # broadcast a user follows other user event
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='events', type='fanout')
        event = {
            "type": "following",
            "origin": self.request.user.pk,
            "target": serializer.data.get('target')
        }
        channel.basic_publish(exchange='events', routing_key='', body=json.dumps(event))
        connection.close()