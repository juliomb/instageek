from django.conf import settings

DEFAULT_IMAGE_SIZE = getattr(settings, 'DEFAULT_IMAGE_SIZE', (500, 500))
DEFAULT_IMAGE_OPTIONS = getattr(settings, 'DEFAULT_IMAGE_OPTIONS', {'size': DEFAULT_IMAGE_SIZE, 'crop': False})
