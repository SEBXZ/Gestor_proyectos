from django.apps import AppConfig

class CommentsConfig(AppConfig):
    name = 'comment'

    def ready(self):
        import comment.signals
