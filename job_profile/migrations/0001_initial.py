# Generated by Django 3.1.7 on 2022-01-07 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='CV Name')),
                ('file', models.FileField(max_length=1000, upload_to='uploads/document/cv/')),
                ('binary_data', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
            ],
        ),
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('summary', models.CharField(max_length=1000, null=True, verbose_name='Summary')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Projects')),
                ('description', models.TextField()),
                ('url', models.URLField(null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Skill')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='Company')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('website', models.URLField(null=True, verbose_name='Website')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Highlight')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.work')),
            ],
        ),
        migrations.CreateModel(
            name='SkillKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Keyword')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.skill')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=50, verbose_name='Technology')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.project')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Website Name')),
                ('link', models.URLField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=200, verbose_name='Institution')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('study_area', models.CharField(max_length=200, verbose_name='Major')),
                ('study_type', models.CharField(max_length=200, verbose_name='Field')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('gpa', models.CharField(max_length=50, verbose_name='GPA')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date', models.DateField()),
                ('awarder', models.CharField(max_length=200, verbose_name='Awarder')),
                ('summary', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('job_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_profile.jobprofile')),
            ],
        ),
    ]
