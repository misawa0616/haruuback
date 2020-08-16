from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from common.utils import uuid_create


class HaruuUser(AbstractUser):
    email = models.EmailField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name_plural = 't1_haruu_user'
        db_table = 't1_haruu_user'


class CustomToken(Token):
    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    key = models.CharField(default=uuid_create, max_length=32)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 't2_custom_token'
        db_table = 't2_custom_token'
