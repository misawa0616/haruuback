from django.db import models
from accounts.models import HaruuUser
from common.utils import uuid_create


class EmailConfirm(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    haruu_user = models.ForeignKey(HaruuUser, blank=True, null=True, on_delete=models.CASCADE)
    after_change_email = models.EmailField(max_length=254)
    token = models.CharField(default=uuid_create, max_length=32)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 't3_email_confirm'
        db_table = 't3_email_confirm'
        verbose_name = 'id'


class FavoriteTag(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    haruu_user = models.ForeignKey(HaruuUser, blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    favorite_url = models.CharField(max_length=254)
    favorite_title = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 't4_favorite_tag'
        db_table = 't4_favorite_tag'
        verbose_name = 'id'


class UserRegisterToken(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    haruu_user = models.ForeignKey(HaruuUser, blank=True, null=True, on_delete=models.CASCADE)
    token = models.CharField(default=uuid_create, max_length=32)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 't5_register_token'
        db_table = 't5_register_token'
        verbose_name = 'id'
