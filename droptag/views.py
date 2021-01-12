from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import tag
from .forms import tagForm, ProfileForm, SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.views.generic import ListView, DetailView
# Create your views here.


class Home(ListView):
    model = tag
    template_name = 'index.html'

class TagDetailView(DetailView):
    model = tag
    template_name = 'tag.html'
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/signup')
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


@login_required(login_url='/signup')
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('homepage')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = SignUpForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'userprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })