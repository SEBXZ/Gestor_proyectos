from users.models import CustomUser
from django.db import models
from django.conf import settings
from users.models import CustomUser

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_users = models.ManyToManyField(CustomUser, related_name='assigned_projects')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    