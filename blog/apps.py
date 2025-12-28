from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    Configures the 'blog' application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
