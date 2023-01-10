from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate

from accounts.forms import SigUpForm, SignInForm


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'accounts/signup.html', context={'form': form, })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('app:index')
        return render(request, 'accounts/signup.html', context={'form': form, })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'accounts/signin.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('app:index')
        return render(request, 'accounts/signin.html', context={
            'form': form,
        })
