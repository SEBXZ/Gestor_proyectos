from django.apps import AppConfig

class ProjectsConfig(AppConfig):
    name = 'project'

    def ready(self):
        import project.signals
