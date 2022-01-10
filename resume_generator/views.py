from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.template import RequestContext, Template
from django.template.loader import render_to_string, get_template

# Create your views here.
from job_profile.models import JobProfile, Link, Education, Work, CV, Award, Project, Skill
from job_profile.models import WorkHighlight, SkillKeyword, ProjectKeyword
from job_profile.forms import JobProfileForm, LinkForm, EducationForm, WorkForm, CVForm

import datetime as dt
import pdfkit

def index(request):
	profiles = JobProfile.objects.all()
	all_cv = CV.objects.all()
	return render(request, 'main/index.html', {'profiles': profiles, 'all_cv': all_cv})

def profile(request, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	return render(request, 'main/profile.html', {'job_profile': profile})


def add_new_profile(request):
	if request.method == 'POST':
		# Add General Profile Detail 
		form = JobProfileForm(request.POST)
		if form.is_valid():
			profile = form.save()
			# Add New Social Links
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					name = request.POST["name-link_"+str(x)]
					link = request.POST["link-link_"+str(x)]
					if name.strip() != "" and link.strip() != "":
						# data = Link(job_profile=job_profile, name=name, link=link)
						data = LinkForm({'job_profile': profile.id, 'name':name, 'link': link})
						if data.is_valid():
							data.save()
						else:
							print(data.errors)
			return redirect('add-profile', 1, profile.id)
		else:
			return HttpResponse(form.errors)		
	else:
		return render(request, 'main/add-profile.html')


def add_profile(request, step, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	if request.method == 'POST':
		if int(step) == 1:
			# Update Education Data
			for edu in profile.education():
				edu.institution = request.POST["institution-edu-"+str(edu.id)]
				edu.location = request.POST["location-edu-"+str(edu.id)]
				edu.study_area = request.POST["study_area-edu-"+str(edu.id)]
				edu.study_type = request.POST["study_type-edu-"+str(edu.id)]
				edu.start_date = request.POST["start_date-edu-"+str(edu.id)]
				edu.end_date = request.POST["end_date-edu-"+str(edu.id)]
				edu.gpa = request.POST["gpa-edu-"+str(edu.id)]
				edu.save()

			# Add New Education Data
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					institution = request.POST["institution-edu_"+str(x)]
					location = request.POST["location-edu_"+str(x)]
					study_area = request.POST["study_area-edu_"+str(x)]
					study_type = request.POST["study_type-edu_"+str(x)]
					start_date = request.POST["start_date-edu_"+str(x)]
					end_date = request.POST["end_date-edu_"+str(x)]
					gpa = request.POST["gpa-edu_"+str(x)]
					if institution.strip() != "" and study_type.strip() != "":
						form = EducationForm({'job_profile': profile.id, 'institution': institution, 
							'location': location, 'study_area': study_area, 'study_type': study_type, 
							'start_date': start_date, 'end_date': end_date, 'gpa': gpa})
						if form.is_valid():
							form.save()
						else:
							print(data.errors)

			# Return Update Work
			return redirect('add-profile', 2, profile.id)
		elif int(step) == 2:
			# Update Work 
			for work in profile.work():
				work.company = request.POST["company-work-"+str(work.id)]
				work.location = request.POST["location-work-"+str(work.id)]
				work.position = request.POST["position-work-"+str(work.id)]
				work.website = request.POST["website-work-"+str(work.id)]
				work.start_date = request.POST["start_date-work-"+str(work.id)]
				work.end_date = request.POST["end_date-work-"+str(work.id)]
				work.save()
				# Update Work Highlights
				for keyword in work.highlights():
					post_name = "name-work-highlight-"+str(work.id)+"-"+str(keyword.id)
					name = request.POST.get(post_name, keyword.name)
					keyword.name = name
					keyword.save()

				# Add new Work Highlights
				form_num = int(request.POST.get("work-highlight_form_num"+str(work.id), 0))
				if form_num > 0:
					form_num = form_num + 1
					for x in range(1, form_num):
						post_name = "name-work-highlight-"+str(work.id)+"_"+str(x)
						name = request.POST.get(post_name, 0)
						if name != 0:
							keyword = WorkHighlight(work=work, name=name)
							keyword.save()

			# Add New Work Data
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					company = request.POST["company-work_"+str(x)]
					location = request.POST["location-work_"+str(x)]
					position = request.POST["position-work_"+str(x)]
					website = request.POST["website-work_"+str(x)]
					start_date = request.POST["start_date-work_"+str(x)]
					end_date = request.POST["end_date-work_"+str(x)]
					if company.strip() != "" and position.strip() != "":
						form = WorkForm({'job_profile': profile.id, 'company': company, 
							'location': location, 'position': position, 'website': website, 
							'start_date': start_date, 'end_date': end_date})
						if form.is_valid():
							work = form.save()
						else:
							print(data.errors)

			# Return Skill Form View
			return redirect('add-profile', 3, profile.id)			
		elif int(step) == 3:
			# Update SKills 
			for skill in profile.skills():
				skill.name = request.POST["name-skill-"+str(skill.id)]
				skill.save()
				# Update Skill KeyWords
				keywords = request.POST["keywords-skill-"+str(skill.id)]
				keywords_dic = keywords.split(',')
				# Get old keywords and Delete them
				skill_keywords = SkillKeyword.objects.filter(skill=skill.id)
				skill_keywords.delete()
				# Add new keywords
				for keyword in keywords_dic:
					new_keyword = SkillKeyword(skill=skill, name=keyword)
					new_keyword.save()

			# Add New Skills
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					name = request.POST["name-skill_"+str(x)]
					if name.strip() != "":
						skill = Skill(job_profile=profile, name=name)
						skill.save()
						# New Skill KeyWords
						keywords = request.POST["keywords-skill_"+str(skill.id)]
						keywords_dic = keywords.split(',')
						for keyword in keywords_dic:
							new_keyword = SkillKeyword(skill=skill, name=keyword)
							new_keyword.save()

			# Return Project Form View
			return redirect('add-profile', 4, profile.id)
		elif int(step) == 4:
			# Update Project 
			for project in profile.projects():
				project.name = request.POST["name-project-"+str(project.id)]
				project.description = request.POST["description-project-"+str(project.id)]
				project.url = request.POST["url-project-"+str(project.id)]
				project.date = request.POST["date-project-"+str(project.id)]
				project.save()
				# Update Project Keywords
				keywords = request.POST['technologies-project-'+str(project.id)]
				keywords_dic = keywords.split(',')
				# Get old keywords and Delete them
				project_keywords = ProjectKeyword.objects.filter(project=project.id)
				project_keywords.delete()
				# Add new keywords
				for keyword in keywords_dic:
					new_keyword = ProjectKeyword(project=project, technology=keyword.strip())
					new_keyword.save()

			# Add New Projects
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					name = request.POST["name-project_"+str(x)]
					description = request.POST["description-project_"+str(x)]
					url = request.POST["url-project_"+str(x)]
					date = request.POST["date-project_"+str(x)]
					if name.strip() != "":
						project = Project(job_profile=profile, name=name, description=description, url=url, 
							date=date)
						project.save()
						# Add Project Keywords
						keywords = request.POST['technologies-project_'+str(x)]
						keywords_dic = keywords.split(',')
						# Add new keywords
						for keyword in keywords_dic:
							new_keyword = ProjectKeyword(project=project, technology=keyword.strip())
							new_keyword.save()

			# Return Award Form View
			return redirect('add-profile', 5, profile.id)
		elif int(step) == 5:
			# Update Awards 
			for award in profile.awards():
				award.title = request.POST["title-award-"+str(award.id)]
				award.date = request.POST["date-award-"+str(award.id)] 
				award.awarder = request.POST["awarder-award-"+str(award.id)] 
				award.summary = request.POST["summary-award-"+str(award.id)]
				award.save()

			# Add New AWards
			form_num = int(request.POST["form_num"])
			if form_num > 0:
				form_num = form_num + 1
				for x in range(1, form_num):
					title = request.POST["title-award_"+str(x)]
					date = request.POST["date-award_"+str(x)] 
					awarder = request.POST["awarder-award_"+str(x)]
					summary = request.POST["summary-award_"+str(x)]
					if title.strip() != "":
						data = Award(job_profile=profile, title=title, date=date, awarder=awarder, 
							summary=summary)
						data.save()

			# Redirect to Profile View
			return redirect('profile', profile.id)
		else:
			return redirect('profile', profile.id)
	else:
		if int(step) == 1:
			return render(request, 'main/add-education.html', {'profile': profile})
		elif int(step) == 2:
			return render(request, 'main/add-work.html', {'profile': profile})
		elif int(step) == 3:
			return render(request, 'main/add-skill.html', {'profile': profile})
		elif int(step) == 4:
			return render(request, 'main/add-project.html', {'profile': profile})
		elif int(step) == 5:
			return render(request, 'main/add-award.html', {'profile': profile})
		else:
			return redirect('index')


def edit_profile(request, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	if request.method == 'POST':
		# Update General Profile Details
		form = JobProfileForm(request.POST, instance=profile)
		if form.is_valid():
			form.save()
		else:
			return HttpResponse(form.errors)
		
		# Update Link
		for link in profile.links():
			name = request.POST["name-link-"+str(link.id)]
			link1 = request.POST["link-link-"+str(link.id)]
			if name.strip() != "" and link1.strip() != "":
				link.name = name
				link.link = link1
				link.save()

		# Add New Link
		form_num = int(request.POST["form_num"])
		if form_num > 0:
			form_num = form_num + 1
			for x in range(1, form_num):
				name = request.POST["name-link_"+str(x)]
				link = request.POST["link-link_"+str(x)]
				if name.strip() != "" and link.strip() != "":
					# data = Link(job_profile=job_profile, name=name, link=link)
					data = LinkForm({'job_profile': profile.id, 'name':name, 'link': link})
					if data.is_valid():
						data.save()
					else:
						print(data.errors)
		# return  
		return redirect('add-profile', 1, profile.id)
	else:
		return render(request, 'main/add-profile.html', {'profile': profile, 'state': 'EDIT'})

def add_cv(request):
	if request.method == 'POST':
		form = CVForm(request.POST, request.FILES)
		if form.is_valid():
			cv = form.save()
			return redirect('view-cv', cv.id)
		else:
			print(form.errors)
			return HttpResponse(form.errors)
	else:
		form = CVForm()
		return render(request, 'main/add-cv.html', {'form': form})


def edit_cv(request, cv_id):
	cv = CV.objects.get(id=int(cv_id))
	if request.method == 'POST':
		form = CVForm(request.POST, request.FILES, instance=cv)
		if form.is_valid():
			cv = form.save()
			return redirect('view-cv', cv.id)
		else:
			return HttpResponse(form.errors)
	else:
		form = CVForm(instance=cv)
		return render(request, 'main/add-cv.html', {'cv': cv, 'form': form, 'state': 'EDIT'})


def cv_view(request, cv_id):
	profiles = JobProfile.objects.all()
	if profiles.count() > 0:
		profile = profiles[0]
		today = dt.datetime.today()
		if cv_id > 0:
			cv = CV.objects.get(id=int(cv_id))
			if cv.file_extension() == 'html':
				cv_html = cv.file.read().decode()
				context = RequestContext(request, {'today': today, 'job_profile': profile})
				template = Template(cv_html)
				return HttpResponse(template.render(context))
			else:
				pass
		else:
			return render(request, 'cv/default-cv.html', {'job_profile': profile, 'today': today})
	else:
		return HttpResponse("Create Profile First")


def pick_cv(request, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	all_cv = CV.objects.all()
	return render(request, 'main/pick-cv.html', {'profile': profile, 'all_cv': all_cv})


def preview_cv(request, cv_id, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	if cv_id > 0:
		cv = CV.objects.get(id=int(cv_id))
		return render(request, 'main/cv-view.html', {'cv': cv, 'profile': profile})
	else:
		return render(request, 'main/cv-view.html', {'profile': profile, 'cv': None})


def cv_iframe_view(request, cv_id, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	today = dt.datetime.today()
	if cv_id > 0:
		cv = CV.objects.get(id=int(cv_id))
		if cv.file_extension() == 'html':
			cv_html = cv.file.read().decode()
			context = RequestContext(request, {'today': today, 'job_profile': profile})
			template = Template(cv_html)
			return HttpResponse(template.render(context))
		else:
			pass
	else:
		return render(request, 'cv/default-cv.html', {'job_profile': profile, 'today': today})


def generate_cv_pdf(request, cv_id, profile_id):
	profile = JobProfile.objects.get(id=int(profile_id))
	pdf = None
	cv_name = 'default-cv'
	today = dt.datetime.today()
	options = {
		'page-size': 'Letter',
		'encoding': "UTF-8",
	}
	if cv_id > 0:
		cv = CV.objects.get(id=int(cv_id))
		if cv.file_extension() == 'html':
			cv_html = cv.file.read().decode()
			context = RequestContext(request, {'today': today, 'job_profile': profile})
			template = Template(cv_html)
			cv_name = cv.name
			pdf = pdfkit.from_string(template.render(context), False, options)

	if pdf == None:
		template = get_template('cv/default-cv.html')
		html = template.render({'today': today, 'job_profile': profile})
		pdf = pdfkit.from_string(html, False, options)
	# buffer.seek(0)
	response = HttpResponse(pdf, content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="'+cv_name+'.pdf"'
	return response


