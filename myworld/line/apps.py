from django.apps import AppConfig


class LineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "line"
    # This function is the only new thing in this file
    # it just imports the signal file when the app is ready
    def ready(self):
        import line.signals
