from rest_framework import serializers
from .models import Project
from task.serializers import TaskSerializer
from django.contrib.auth import get_user_model

User = get_user_model()
class ProjectSerializer(serializers.ModelSerializer):
    tasks= TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at', 'updated_at']

