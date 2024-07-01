import logging
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Project
from notifications.models import Notification
from users.models import CustomUser

logger = logging.getLogger(__name__)


@receiver(m2m_changed, sender=Project.assigned_users.through)
def notify_users_on_assignment(sender, instance, action, reverse, pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            user = CustomUser.objects.get(pk=user_id)
            Notification.objects.create(
                user=user,
                message=f"Te asignaron al proyecto: '{instance.name}'."
            )
