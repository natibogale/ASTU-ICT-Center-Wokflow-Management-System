# Generated by Django 3.2.4 on 2021-10-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0004_projects_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmessages',
            name='isFirstMessage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectTitle',
            field=models.CharField(max_length=50, verbose_name='Project Title'),
        ),
    ]