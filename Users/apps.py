from django.apps import AppConfig
from . import signals
class UsersConfig(AppConfig):
    name = 'Users'

    def ready(self):
        import users.signals
