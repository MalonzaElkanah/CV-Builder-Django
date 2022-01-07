from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

import django.utils.timezone as tz


class JobProfile(models.Model):
	title = models.CharField('Title', max_length=150)
	first_name = models.CharField('First Name', max_length=50)
	middle_name = models.CharField('Middle Name', max_length=50)
	last_name = models.CharField('Last Name', max_length=50)
	email = models.CharField('Email', max_length=50)
	phone_number = models.CharField('Phone Number', max_length=50)
	location = models.CharField('Location', max_length=50)
	summary = models.CharField('Summary', max_length=1000, null=True)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# user, title, first_name, middle_name, last_name, email, phone_number, location, summary

	def links(self):
		return Link.objects.filter(job_profile=self.id)

	def education(self):
		return Education.objects.filter(job_profile=self.id)

	def work(self):
		return Work.objects.filter(job_profile=self.id)

	def skills(self):
		return Skill.objects.filter(job_profile=self.id)

	def projects(self):
		return Project.objects.filter(job_profile=self.id)

	def awards(self):
		return Award.objects.filter(job_profile=self.id)


class Link(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	name = models.CharField('Website Name', max_length=50)
	link = models.URLField()
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, name, link


class Education(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	institution = models.CharField('Institution', max_length=200)
	location = models.CharField('Location', max_length=50)
	study_area = models.CharField('Major', max_length=200)
	study_type = models.CharField('Field', max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	gpa = models.CharField('GPA', max_length=50)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, institution, location, study_area, study_type, start_date, end_date, gpa


class Work(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	company = models.CharField('Company', max_length=50)
	location = models.CharField('Location', max_length=50)
	position = models.CharField('Position', max_length=50)
	website = models.URLField('Website', null=True)
	start_date = models.DateField()
	end_date = models.DateField()
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, company, location, position, website, start_date, end_date

	def highlights(self):
		return WorkHighlight.objects.filter(work=self.id)


class WorkHighlight(models.Model):
	work = models.ForeignKey(Work, on_delete=models.CASCADE)
	name = models.CharField("Highlight", max_length=500)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# work, name,


class Skill(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	name = models.CharField('Skill', max_length=200)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, name,

	def keywords(self):
		return SkillKeyword.objects.filter(skill=self.id)


class SkillKeyword(models.Model):
	skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
	name = models.CharField('Keyword', max_length=200)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# skill, name,


class Project(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	name = models.CharField('Projects', max_length=200)
	description = models.TextField()
	url = models.URLField(null=True)
	date = models.DateField(default=tz.now)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, name, description, url, date

	def keywords(self):
		return ProjectKeyword.objects.filter(project=self.id)


class ProjectKeyword(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	technology = models.CharField('Technology', max_length=50)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# project, technology,


class Award(models.Model):
	job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
	title = models.CharField('Title', max_length=200)
	date = models.DateField()
	awarder = models.CharField('Awarder', max_length=200)
	summary = models.TextField()
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# job_profile, title, date, awarder, summary


class CV(models.Model):
	name = models.CharField('CV Name', max_length=50)
	file = models.FileField(upload_to='uploads/document/cv/', max_length=1000)
	binary_data = models.TextField(null=True)
	description = models.TextField(null=True)
	status = models.CharField('Status', max_length=50)
	date_created = models.DateTimeField('Date Created', auto_now_add=True)
	# name, file, binary_data, description, status,

	def file_extension(self):
		path = self.file.path
		file_name = os.path.basename(path)
		file_dictionary = file_name.split('.')
		file_extension = file_dictionary[-1]
		return file_extension

