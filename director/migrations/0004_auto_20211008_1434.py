# Generated by Django 3.2.4 on 2021-10-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0003_auto_20211008_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='assistantApproved',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Approve report from Team'),
        ),
        migrations.AddField(
            model_name='reports',
            name='assistantApprovedDate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Approve Report from Team'),
        ),
    ]