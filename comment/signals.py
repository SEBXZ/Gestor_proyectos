from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from task.models import Task
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def create_notification_for_comment(sender, instance, created, **kwargs):
    if created:
        task = instance.task
        assigned_user = task.assigned_to
        Notification.objects.create(
            user=assigned_user,
            message=f"A new comment was added to your task '{instance.task}'."
        )
