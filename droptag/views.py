from .models import tag, UserProfile
from .forms import tagForm, UpdateTagForm, UserProfileForm, UserRegisterForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
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


#experimental
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
            #return reverse_lazy('login')
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = UserRegisterForm()
        p_reg_form = UserProfileForm()
        
    context = {
        'form': form,
        'p_reg_form': p_reg_form
    }
    return render(request, 'register.html', context)



    
