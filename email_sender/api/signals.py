from api.encrypt import encryption_service
from api.models import Mail, User
from app_celery.tasks import create_periodic_task
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_task(sender, **kwargs):
    if kwargs.get("created"):
        tg_id = kwargs.get("instance").tg_id
        create_periodic_task(tg_id)


@receiver(pre_save, sender=Mail)
def encrypt_pass(sender, instance: Mail, **kwargs):
    if instance.pk is None:
        instance.password = encryption_service.encrypt(password=instance.password)
