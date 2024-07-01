from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task
from notifications.models import Notification

@receiver(post_save, sender=Task)
def notify_user_assigned_to_task(sender, instance, created, **kwargs):
    if created:
        assigned_user = instance.assigned_to
        Notification.objects.create(
            user=assigned_user,
            message=f"You have been assigned a new task: '{instance.name}'."
        )
