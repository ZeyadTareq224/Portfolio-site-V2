from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('pages-home')
		else:
			messages.info(request, "Sorry!, this form is only for the authorized users.")	
	context = {}
	return render(request, 'user/login_page.html', context)

@login_required()
def logout_page(request):
	logout(request)
	return redirect('pages-home')	