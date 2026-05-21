from django.apps import AppConfig


class MusicConfig(AppConfig):
    name = 'music'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Import signals if you add them later
        pass
