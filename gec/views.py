from __future__ import absolute_import
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from braces import views
from .forms import RegistrationForm, LoginForm

def home_page(request):
    return render(request, 'gec/home.html')

class SignUpView(views.AnonymousRequiredMixin,
                 views.FormValidMessageMixin,
                 generic.CreateView):
    form_class = RegistrationForm
    form_valid_message = 'you have successfully signed up'
    success_url = reverse_lazy('home')
    model = User
    template_name = 'gec/signup.html'


class LoginView(views.AnonymousRequiredMixin,
                views.FormValidMessageMixin,
                generic.FormView):
    form_class = LoginForm
    form_valid_message = 'you are logged in'
    success_url = reverse_lazy('home')
    template_name = 'gec/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin,
                 views.MessageMixin,
                 generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.messages.success("You've been logged out. Come back soon!")
        return super().get(request, *args, **kwargs)
