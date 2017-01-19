from django.contrib.auth.models import User
from django.db import models



class Relationship(models.Model):

    origin = models.ForeignKey(User, related_name='relationship_origin')
    target = models.ForeignKey(User, related_name='relationship_target')
    created_at = models.DateTimeField(auto_now_add=True)
