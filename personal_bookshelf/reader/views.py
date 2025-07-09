from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomLoginForm
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

