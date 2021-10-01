# Generated by Django 3.2.4 on 2021-10-01 19:04

import director.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0005_auto_20210930_1427'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('projectTitle', models.CharField(max_length=500, verbose_name='Project Title')),
                ('projectDescription', models.TextField(verbose_name='Project Description')),
                ('deadLine', models.DateField(verbose_name='Project DeadLine')),
                ('is_seen', models.BooleanField(default=False)),
                ('is_urgent', models.BooleanField(default=False)),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('projectFile', models.FileField(blank=True, upload_to='project_documents/', validators=[director.models.validate_file], verbose_name='Project File')),
                ('assignedTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Assign Project to')),
                ('created_by', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Project Created By')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(verbose_name='Message')),
                ('projectMessageFile', models.FileField(blank=True, upload_to='message_documents/', validators=[director.models.validate_file], verbose_name='Message File')),
                ('sentDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Sent')),
                ('is_seen', models.BooleanField(default=False)),
                ('messageSender', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Message From')),
                ('messageTo', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Message To')),
                ('projectId', models.ForeignKey(max_length=500, on_delete=django.db.models.deletion.CASCADE, to='director.projects', verbose_name='Project ID')),
            ],
            options={
                'verbose_name_plural': 'Project Messages',
            },
        ),
    ]
