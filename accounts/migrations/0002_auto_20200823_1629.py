# Generated by Django 2.2.14 on 2020-08-23 07:29

import common.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='haruuuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='haruuuser',
            name='username',
            field=models.CharField(default=common.utils.uuid_create, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username'),
        ),
        migrations.CreateModel(
            name='RegisterToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default=common.utils.uuid_create, max_length=32)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('haruu_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'id',
                'verbose_name_plural': 't5_register_token',
                'db_table': 't5_register_token',
            },
        ),
    ]
