from django.apps import AppConfig

class TasksConfig(AppConfig):
    name = 'task'

    def ready(self):
        import task.signals
