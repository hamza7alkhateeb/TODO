import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task


logger = logging.getLogger('tasks')

@receiver(post_save, sender=Task)
def task_created(sender,instance, created, **kwargs):
    if created:
        print(f"New Task created: {instance.title} (User:  {instance.user})")
        logger.info(f"New Task created: {instance.title} (User:  {instance.user})")