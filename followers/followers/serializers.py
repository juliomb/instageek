from django.utils.translation import ugettext as _
from rest_framework import serializers

from followers.models import Relationship


class RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relationship
        read_only_fields = ('origin',)
        fields = '__all__'


    def validate(self, attrs):
        request_user = self.context.get('request').user.pk
        if request_user == attrs.get('target'):
            raise serializers.ValidationError(_('You can not follow yourself.'))
        if Relationship.objects.filter(origin=request_user, target=attrs.get('target')).exists():
            raise serializers.ValidationError(_('You are already following this user.'))

        """
        # example of how to validate that target user exists, colaborating with another microservice
        response = requests.get('http://localhost:8001/user/{0}'.format(attrs.get('target')))
        if response.status_code == 404:
            raise serializers.ValidationError(_("Target user doesn't exist'"))
        """

        return attrs