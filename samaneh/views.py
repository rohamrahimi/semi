from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
from samaneh.forms import SignUpForm, LoginForm, User

user = None


def home_page(request):
    return render(request, 'samaneh/homepage.html')


def signup(request):
    form = SignUpForm()
    error = None
    context = {'form': form, 'error':error}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form.is_valid()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        pass2 = form.cleaned_data.get('password2')
        if not pass2 == raw_password:
            error = 'گذرواژه و تکرار گذرواژه یکسان نیستند'
        try:
            user = User.objects.get(username=username)
        except:
            error = 'نام کاربری شما در سیستم موجود است'
        if error:
            context['error'] = error
            return render(request, 'signup.html', context)
        form.save()
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


def contact(request):
    return render(request, 'contact.html')


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
