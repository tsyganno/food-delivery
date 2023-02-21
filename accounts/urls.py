from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings

from accounts.views import SignUpView, SignInView, NewPasswordResetView, NewPasswordResetDone, NewPasswordResetConfirmView, NewPasswordResetCompleteView

app_name = 'acc'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(),  name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('reset_password/', NewPasswordResetView.as_view(),  name='reset_password'),
    path('password_reset/done/', NewPasswordResetDone.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>/', NewPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/done/', NewPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
