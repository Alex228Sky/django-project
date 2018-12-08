from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
	return render(request, 'user_example/index.html')

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('http://localhost:8000')
	else:
		form = UserCreationForm()



	context = {'form' : form}
	return render(request, 'registration/register.html', context)

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


