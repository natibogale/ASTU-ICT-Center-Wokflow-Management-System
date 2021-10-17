# Generated by Django 3.2.4 on 2021-10-08 11:23

import director.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='reportFile',
            field=models.FileField(blank=True, upload_to='report_documents/', validators=[director.models.validate_file], verbose_name='Report File'),
        ),
    ]