from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from task.models import Task
from users.models import CustomUser

class ProjectSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        total_projects = Project.objects.count()
        completed_tasks = Task.objects.filter(status='completed').count()
        active_users = CustomUser.objects.filter(is_active=True).count()

        data = {
            'total_projects': total_projects,
            'completed_tasks': completed_tasks,
            'active_users': active_users,
        }
        return Response(data)
class TaskSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        total_tasks = Task.objects.count()
        completed_tasks = Task.objects.filter(status='completed').count()
        pending_tasks = Task.objects.filter(status='pending').count()

        data = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
        }
        return Response(data)
