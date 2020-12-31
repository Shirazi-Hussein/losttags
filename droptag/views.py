from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import tag
from .forms import tagForm
from django.contrib import messages 
# Create your views here.

def home(request):
    tags = tag.objects.all()
    return render(request, 'index.html', {'Tags':tags})

def form_detail(request): 
    if request.method == 'POST':
        form = tagForm(request.POST)
        if form.is_valid():
            obj = form.save(commit = False) 
            obj.user = request.user; 
            obj.save() 
            form = tagForm() 
            messages.success(request, "Successfully created") 
            
    else:
        form = tagForm()
        
    return render(request, 'name.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
