# Generated by Django 3.2.4 on 2021-10-08 14:00

import assistant_director.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0005_auto_20210930_1427'),
        ('director', '0003_auto_20211008_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssistantMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('reportMessageFile', models.FileField(blank=True, upload_to='message_documents/', validators=[assistant_director.models.validate_file], verbose_name='Message File')),
                ('sentDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Sent')),
                ('isFirstMessage', models.BooleanField(default=False)),
                ('is_seen', models.BooleanField(default=False)),
                ('messageSender', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Message From')),
                ('messageTo', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Message To')),
                ('reportId', models.ForeignKey(max_length=500, on_delete=django.db.models.deletion.CASCADE, to='director.reports', verbose_name='Report ID')),
            ],
            options={
                'verbose_name_plural': 'Assistant Director Report Messages',
            },
        ),
        migrations.CreateModel(
            name='ApproveReportTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('assistantApproved', models.BooleanField(default=False, verbose_name='Approve report from Team')),
                ('assistantApprovedDate', models.DateField(blank=True, default=None, null=True, verbose_name='Approve Report from  Team')),
                ('team', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Team')),
            ],
            options={
                'verbose_name_plural': 'Approve reports from teams',
            },
        ),
    ]
