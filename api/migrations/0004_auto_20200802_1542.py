# Generated by Django 2.2.14 on 2020-08-02 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200802_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emailconfirm',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
