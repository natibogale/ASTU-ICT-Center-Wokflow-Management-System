# Generated by Django 3.2.4 on 2021-10-05 07:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('director', '0003_auto_20211004_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TemProjectMessages',
            new_name='TeamProjectMessages',
        ),
        migrations.AddField(
            model_name='projects',
            name='is_late',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]