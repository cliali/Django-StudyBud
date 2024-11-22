from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_studybud.core"

    # def ready(self) -> None:
    #     import django_studybud.core.signals.handlers
