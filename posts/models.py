from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

from posts.settings import DEFAULT_IMAGE_OPTIONS


class Post(models.Model):

    owner = models.ForeignKey(User)
    description = models.TextField()
    image = ThumbnailerImageField(resize_source=DEFAULT_IMAGE_OPTIONS)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
