# Generated by Django 3.1.7 on 2022-01-07 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_profile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobprofile',
            name='user',
        ),
    ]
