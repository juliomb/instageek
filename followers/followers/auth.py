import json

from django.utils.encoding import smart_text
from rest_framework.authentication import BaseAuthentication, get_authorization_header


class FakeUser(object):

    def __init__(self, id, username):

        self.pk = id
        self.id = id
        self.username = username



class JSONAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_header = smart_text(get_authorization_header(request))
        user_data = json.loads(auth_header)
        return FakeUser(user_data.get('id'), user_data.get('username')), "JSONAuth"
