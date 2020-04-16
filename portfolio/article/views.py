from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


# Create your views here.
def index(request):
    photo = Photo.objects.all()

    context = {
        'photos': photo
    }
    return render(request, 'article/photos.html', context)

 

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
    else: 
        form = AuthenticationForm()
    return render(request, 'article/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


@login_required(login_url="../login/")
def article_create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
    else:
        form = PhotoForm()
    context = {
        'form': form
    }
    return render(request, 'article/add.html', context)