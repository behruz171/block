from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_token_for_user(sender, instance=None, created=False, **kwargs):
    if created:
        for user in User.objects.all():
            Token.objects.get_or_create(user=user)
