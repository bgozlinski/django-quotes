from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages


# Create your views here.
def signup_user(request):
    if request.user.is_authenticated:
        return redirect(to='quoteapp:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'registration/signup.html', {'form': form})

    return render(request, 'registration/signup.html', {'form': RegisterForm()})


def login_user(request):
    if request.user.is_authenticated:
        return redirect(to='quoteapp:main')

    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quoteapp:main')

    return render(request, 'registration/login.html', {'form': LoginForm()})


@login_required
def logout_user(request):
    logout(request)
    return redirect(to='quoteapp:main')





