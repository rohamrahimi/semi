from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from samaneh.forms import SignUpForm, LoginForm, Contact


def home_page(request):
    return render(request, 'samaneh/homepage.html')


def signup(request):
    form = SignUpForm()
    errors = []
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
        if User.objects.filter(username=form.data['username']).exists():
            errors.append('نام کاربری شما در سیستم موجود است')
        if form.data['password1'] != form.data['password2']:
            errors.append('گذرواژه و تکرار گذرواژه یکسان نیستند')
    context = {'form': form, 'errors': errors}
    return render(request, 'signup.html', context)


def login(request):
    form = LoginForm()
    context = {'form': form }
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass


def contact(request):
    form = Contact()
    if request.method == 'POST':
        form = Contact(request.POST)
        print('ali')
        if form.is_valid():
            return redirect('/contacted')
    context = {'form': form}
    return render(request, 'contact.html', context)


def contacted(request):
    return render(request, 'contacted.html')
