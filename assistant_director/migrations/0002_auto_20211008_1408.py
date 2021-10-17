# Generated by Django 3.2.4 on 2021-10-08 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20210930_1427'),
        ('assistant_director', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvereportteam',
            name='assistantApproved',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Approve report from Team'),
        ),
        migrations.AlterField(
            model_name='approvereportteam',
            name='team',
            field=models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Team'),
        ),
    ]