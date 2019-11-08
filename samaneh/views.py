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
    errors = list()
    context = {'form': form, 'errors': errors}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username=username, password=raw_password)
            auth.login(request, user)
            return redirect('/')
        else:
            if not request.POST.get('password1') == request.POST.get('password2'):
                errors.append('گذرواژه و تکرار گذرواژه یکسان نیستند')

            if User.objects.filter(username=form.data['username']).exists():
                errors.append('نام کاربری شما در سیستم موجود است')

            if len(errors) > 0:
                context['errors'] = errors
                return render(request, 'signup.html', context)

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


def profile(request):
    if request.user.is_authenticated:
        context = {'username': request.user.username,
                   'first_name': request.user.first_name,
                   'last_name': request.user.last_name}
        return render(request, 'profile.html', context)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def go_panel(request):
    return render(request, 'panel.html')

def setting(request):
    pass

