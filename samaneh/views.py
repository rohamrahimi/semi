from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from samaneh.forms import SignUpForm, LoginForm


def home_page(request):
    return render(request, 'samaneh/homepage.html')


def signup(request):
    form = SignUpForm()
    context = {'form': form}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html', context)


def login(request):
    form = LoginForm()
    context = {'form': form}
    error = False
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'samaneh/homepage.html', context)
        else:
            error = True
    context['error'] = error
    return render(request, 'login.html', context)
