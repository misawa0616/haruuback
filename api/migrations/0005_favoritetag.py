# Generated by Django 2.2.14 on 2020-08-15 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20200802_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=254)),
                ('title', models.CharField(max_length=254)),
                ('class_id', models.CharField(max_length=254)),
                ('haruu_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'id',
                'verbose_name_plural': 't4_favorite_tag',
                'db_table': 't4_favorite_tag',
            },
        ),
    ]
