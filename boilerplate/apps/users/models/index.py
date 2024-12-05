from django.contrib.auth.models import AbstractUser

from boilerplate.bases.models import Model


# Main Section
class User(AbstractUser, Model):
    groups = None
    user_permissions = None

    class Meta:
        verbose_name = verbose_name_plural = "유저"
