# Generated by Django 3.2.4 on 2021-10-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_leader', '0002_alter_expertprojectmessages_projectunique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertprojectmessages',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Message'),
        ),
    ]
