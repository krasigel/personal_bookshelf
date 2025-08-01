from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomLoginForm, EditProfileForm
from django.contrib.auth.views import LogoutView, LoginView


class ReaderRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'reader/register.html'
    success_url = reverse_lazy('login')


class ReaderLoginView(LoginView):

    template_name = 'reader/login.html'
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy('bookshelf')


class ReaderLogoutView(LogoutView):

    next_page = 'login'


class EditProfileView(LoginRequiredMixin, UpdateView):

    model = CustomUser
    form_class = EditProfileForm
    template_name = 'reader/edit_profile.html'
    success_url = reverse_lazy('bookshelf')

    def get_object(self):
        return self.request.user


class DeleteProfileView(LoginRequiredMixin, DeleteView):

    model = CustomUser
    template_name = 'reader/delete_profile.html'
    success_url = reverse_lazy('register')

    def get_object(self):
        return self.request.user
