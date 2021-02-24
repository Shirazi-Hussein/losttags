from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView


class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('edit_profile')
    template_name = 'registration/change-password.html'


