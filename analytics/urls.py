from django.urls import path
from .views import ProjectSummaryView, TaskSummaryView

urlpatterns = [
    path('project-summary/', ProjectSummaryView.as_view(), name='project-summary'),
    path('task-summary/', TaskSummaryView.as_view(), name='task-summary'),
]
