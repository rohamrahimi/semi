from django.contrib.auth import authenticate, login
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
            login(request, user)
            return redirect('/')
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
