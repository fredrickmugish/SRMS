from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import*

def index(request):
    course = Course.objects.all()
    context = {'courses': course}
    return render(request, 'site_index.html', context)

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
    return redirect('login_user')

def dashboard(request):
    return render(request, 'user_panel.html')

def registration(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'registration.html', context)

def registrationAdd(request):
    if request.method == 'POST':
        # Handle form submission
        full_name = request.POST.get('full_name')
        course_id = request.POST.get('course')
        application_form = request.FILES.get('application_form')
        
        # Save data to the database
        registration = Registration()
        registration.full_name = full_name
        registration.course_id = course_id
        registration.application_form = application_form
        registration.save()

        

        messages.success(request, 'Registered successfully!')

        return HttpResponseRedirect('/registration/')  
 # Retrieve courses for the dropdown
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'registration.html', context)

def about(request):
    return render(request, 'site_about.html')

def site_courses(request):
    course = Course.objects.all()
    context = {'courses': course}
    return render(request, 'site_courses.html', context)

def contact(request):
    return render(request, 'site_contact.html')

def fee(request):
    payments = Payment.objects.all()  # or use appropriate filter if needed
    return render(request, 'fee.html', {'payments': payments})