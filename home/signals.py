from home.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from student.models import Code


@receiver(post_save, sender = User)
def post_savegenerate_code_code(sender, instance, created,*args, **kwargs):
    if created:
        Code.objects.create(user=instance)
        