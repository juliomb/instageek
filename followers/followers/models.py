from django.db import models



class Relationship(models.Model):

    unique_together = ('origin', 'target')  # con sqlite no sirve, funcionaria con postgresql o mysql

    origin = models.IntegerField()
    target = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
