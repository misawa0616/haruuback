from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from common.utils import uuid_create
from django.utils.translation import gettext_lazy as _


class HaruuUser(AbstractUser):
    username = models.CharField(
        _('username'),
        default=uuid_create,
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(blank=True, unique=True)
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
