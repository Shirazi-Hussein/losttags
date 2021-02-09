from .models import tag, UserProfile
from .forms import tagForm, UpdateTagForm, UserProfileForm, UserRegisterForm, EditUserProfileForm, PasswordChangingForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView
import json
# Create your views here.


class Home(ListView):
    model = tag
    template_name = 'index.html'
    queryset = tag.objects.order_by('-date_filled')[0:3]
    
    
class AllTags(ListView):
    model = tag
    template_name = 'alltags.html'
    queryset = tag.objects.order_by('-date_filled')


class TagDetailView(DetailView):
    model = tag
    template_name = 'tag.html'


class CreateTag(LoginRequiredMixin, CreateView):
    login_url = '/users/login'
    redirect_field_name = 'login'
    
    model = tag
    form_class = tagForm
    template_name = "createtag.html"
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class UpdateTag(LoginRequiredMixin, UpdateView):
    login_url = '/users/login'
    redirect_field_name = 'login'
    
    model = tag
    form_class = UpdateTagForm
    template_name = 'update_tag.html'


class DeleteTag(LoginRequiredMixin, DeleteView):
    login_url = '/users/login'
    redirect_field_name = 'login'
    
    model = tag
    template_name = "deletetag.html"
    success_url = reverse_lazy('homepage')


def ViewProfile(request, user):
    profile = UserProfile.objects.get(user=user)
    return render(request, 'viewprofile.html', {'profile':profile})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        p_reg_form = UserProfileForm(request.POST)
        if form.is_valid() and p_reg_form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            p_reg_form = UserProfileForm(request.POST, instance=user.userprofile)
            p_reg_form.full_clean()
            p_reg_form.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = UserRegisterForm()
        p_reg_form = UserProfileForm()
        
    context = {
        'form': form,
        'p_reg_form': p_reg_form
    }
    return render(request, 'register.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditUserProfileForm(request.POST, instance=request.user.userprofile)

        if profile_form.is_valid():
            custom_form = profile_form.save(False)
            custom_form.save()
            return HttpResponseRedirect(reverse('homepage'))
    else:
        profile_form = EditUserProfileForm(instance=request.user.userprofile)
        args = {}
        args['profile_form'] = profile_form
        return render(request, 'edit_profile.html', args)


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('edit_profile')
    template_name = 'change-password.html'
    



    
