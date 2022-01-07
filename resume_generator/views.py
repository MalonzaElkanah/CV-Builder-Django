from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from job_profile.models import JobProfile, Link, Education, Work, CV, Award, Project, Skill

def index(request):
	profiles = JobProfile.objects.all()
	all_cv = CV.objects.all()
	return render(request, 'main/index.html', {'profiles': profiles, 'all_cv': all_cv})

def profile(request):
	return render(request, 'main/index.html')

def add_profile(request, step):
	if request.method == 'POST':
		pass
	else:
		if int(step) == 1:
			return render(request, 'main/add-profile.html')
		elif int(step) == 2:
			return render(request, 'main/add-education.html')
		elif int(step) == 3:
			return render(request, 'main/add-work.html')
		elif int(step) == 4:
			return render(request, 'main/add-skill.html')
		elif int(step) == 5:
			return render(request, 'main/add-project.html')
		elif int(step) == 6:
			return render(request, 'main/add-award.html')
		else:
			return redirect('index')


def edit_profile(request):
	return render(request, 'main/index.html')


