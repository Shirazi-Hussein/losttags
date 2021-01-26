from .models import tag
from .forms import tagForm, UpdateTagForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class Home(ListView):
    model = tag
    template_name = 'index.html'
    #view how many recent tags you want on 'home'
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
    
