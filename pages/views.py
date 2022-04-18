from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from . forms import ProjectForm, CertificateForm
from .models import Project, Certificate
from django.contrib.auth.decorators import login_required


def home_page(request):

	context = {}
	return render(request, 'pages/home_page.html', context)


def portofolio(request):
	projects = Project.objects.all().order_by('-id')
	context = {'projects': projects}
	return render(request, 'pages/portofolio.html', context)

@login_required(login_url='portofolio')
def create_project(request):
	form = ProjectForm()
	if request.method == "POST":
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('portofolio')
	context = {'form': form}
	return render(request, 'pages/project_form.html', context)

@login_required(login_url='portofolio')
def update_project(request, pk):
	project = Project.objects.get(id=pk)

	form = ProjectForm(instance=project)
	if request.method == "POST":
		form = ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect('portofolio')
	context = {'form': form}
	return render(request, 'pages/project_form.html', context)

@login_required(login_url='portofolio')
def delete_project(request, pk):
	project = Project.objects.get(id=pk)

	if request.method == "POST":
		project.delete()
		return redirect('portofolio')
	context = {'project': project}
	return render(request, 'pages/project_delete.html', context)


def details_project(request, pk):
	project = Project.objects.get(id=pk)

	context = {'project': project}
	return render(request, 'pages/project_details.html', context)


def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		subject = request.POST['subject']
		email = request.POST['email']
		name_email = "sender name: " + name + " sender email: " + email + " subject: " + subject
		message = request.POST['message']
		send_mail(
			name_email,
			message,
			email,
			['ziyadtr101@gmail.com']
		)
		context = {'name':name}
		return render(request, 'pages/contact.html', context)
	else:
		return render(request, 'pages/contact.html')

def certificates(request):
	certificates = Certificate.objects.all().order_by('-id')

	context = {'certificates': certificates}
	return render(request, 'pages/certificates.html', context)

@login_required(login_url='certificates')
def create_certificate(request):
	form = CertificateForm()
	if request.method == "POST":
		form = CertificateForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('certificates')
	context = {'form': form}
	return render(request, 'pages/certificate_form.html', context)

@login_required(login_url='certificates')
def delete_certificate(request, pk):
	certificate = Certificate.objects.get(id=pk)
	if request.method == "POST":
		certificate.delete()
		return redirect('certificates')	
	context = {'certificate': certificate}	
	return render(request, 'pages/delete_certificate.html', context)

@login_required(login_url='certificates')
def update_certificate(request, pk):
	certificate = Certificate.objects.get(id=pk)
	form = CertificateForm(instance=certificate)
	if request.method == "POST":
		form = CertificateForm(request.POST, request.FILES, instance=certificate)
		if form.is_valid():
			form.save()
			return redirect('certificates')

	context = {'form': form}
	return render(request, 'pages/certificate_form.html', context)


def certificate_details(request, pk):
	certificate	= Certificate.objects.get(id=pk)

	context = {'certificate': certificate}
	return render(request, 'pages/certificate_details.html', context)