from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, Addbook
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import Books
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout, login 


def index(reqest):
    book = Books.objects.all()
    return render(reqest, 'index.html', {'book' : book})



def signin(reqest):
    if reqest.method == 'POST':
        form = UserRegisterForm(reqest.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(reqest, f'hi{username}')
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            login(reqest, user)
            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    return render(reqest,'registration/signin.html', {'form': form})

def about(reqest):
    return render(reqest,'about.html')

def chat(reqest):
    return render(reqest,'chat.html')

@csrf_exempt
def lib(reqest):
    form = Addbook(reqest.POST or None, reqest.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user_id = reqest.user
        instance.save()
        #current_user = reqest.user
        #print(current_user.id)
        return HttpResponseRedirect('/')
    book = Books.objects.filter(user_id=reqest.user)
    return render(reqest,'lib.html',{'form' : form,'book': book})

def account(reqest):
    return render(reqest,'account.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')
