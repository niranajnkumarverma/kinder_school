from django.apps import AppConfig


class UsernotifierConfig(AppConfig):
    name = 'usernotifier'
    def ready(self):
        from usernotifier import signals
