from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        requested_user = request.POST['username']
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=requested_user)
                return render(request, 'accounts/signup.html',
                              {'error': 'Username already in use'})
            except User.DoesNotExist:
                new_user = User.objects.create_user(
                    requested_user, password=request.POST['password1'])
                auth.login(request, new_user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',
                          {'error': 'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',
                          {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
