from django import forms
from django.forms import ModelForm
from .models import JobProfile, Education, Work, Link


class JobProfileForm(ModelForm):
	class Meta:
		model = JobProfile
		fields = ('title', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'location', 'summary')


class EducationForm(ModelForm):
	class Meta:
		model = Education
		fields = ('job_profile', 'institution', 'location', 'study_area', 'study_type', 
			'start_date', 'end_date', 'gpa')


class WorkForm(ModelForm):
	class Meta:
		model = Work
		fields = ('job_profile', 'company', 'location', 'position', 'website', 'start_date', 'end_date')


class LinkForm(ModelForm):
	class Meta:
		model = Link
		fields = ('job_profile', 'name', 'link')
		