# Generated by Django 3.2.4 on 2021-10-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0001_initial'),
        ('team_leader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertprojectmessages',
            name='projectUnique',
            field=models.ForeignKey(blank=True, max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='director.projects', to_field='expertUnique'),
        ),
    ]