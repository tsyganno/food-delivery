from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from accounts.forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('acc:signin')


class SignInView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/signin.html'


class NewPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('acc:password_reset_done')


class NewPasswordResetDone(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class NewPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('acc:password_reset_complete')


class NewPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'
