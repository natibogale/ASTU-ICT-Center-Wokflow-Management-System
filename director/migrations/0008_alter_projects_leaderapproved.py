# Generated by Django 3.2.4 on 2021-10-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0007_auto_20211007_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='leaderApproved',
            field=models.BooleanField(default=False, verbose_name='Approve Project Submission From Experts'),
        ),
    ]