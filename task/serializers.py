from rest_framework import serializers
from .models import Task
from comment.serializers import CommentSerializer
from Attachmen.serializers import AttachmentSerializer
class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'  