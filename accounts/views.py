from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from accounts.forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('acc:signin')


class SignInView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/signin.html'
