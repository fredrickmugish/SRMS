from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'site_index.html')

def login_user(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect(reverse('admin:index'))  # Redirect to Jazzmin admin panel
        else:
            return redirect('user_panel')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect(reverse('admin:index'))  # Redirect to Jazzmin admin panel
                else:
                    return redirect('user_panel')
            else:
                messages.info(request, 'Username OR password is incorrect')

    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect(reverse('admin:index'))  # Redirect to Jazzmin admin panel
        else:
            return redirect('user_panel')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {user}')
                return redirect('index')

        return render(request, 'register.html', {'form': form})


def user_panel(request):
    return render(request, 'user_panel.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def dashboard(request):
    return render(request, 'user_panel.html')

def registration(request):
    return render(request, 'registration.html')
def about(request):
    return render(request, 'site_about.html')
def site_courses(request):
    return render(request, 'site_courses.html')
def contact(request):
    return render(request, 'site_contact.html')