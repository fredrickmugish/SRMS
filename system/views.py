from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import*
from django.contrib.auth.decorators import login_required
from .forms import CustomPasswordChangeForm
from .forms import ProfileForm
from .models import Profile

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
                return redirect('login_user')

        return render(request, 'register.html', {'form': form})


@login_required
def user_panel(request):
    registrations = Registration.objects.filter(user=request.user)
    payments = Payment.objects.filter(registration__user=request.user)
    context = {
        'registrations': registrations,
        'payments': payments,
    }
    return render(request, 'user_panel.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required
def dashboard(request):
    return render(request, 'user_panel.html')

@login_required
def registration(request):
    courses = Course.objects.all()
    # Pass the username of the logged-in user to the template
    context = {
        'courses': courses,
        'username': request.user.username
    }
    return render(request, 'registration.html', context)

@login_required
def registrationAdd(request):
    if request.method == 'POST':
        last_name = request.POST.get('last_name')
        course_id = request.POST.get('course')
        application_form = request.FILES.get('application_form')
        
        # Check if the username is already registered
        if Registration.objects.filter(last_name=last_name).exists():
            messages.error(request, 'A registration with this name already exists.')
            return redirect('registration')  # Redirect back to the registration form

        # Save data to the database
        registration = Registration()
        registration.user = request.user  # Associate registration with the logged-in user
        registration.last_name = last_name
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

@login_required
def fee(request):
    # Get payments for the logged-in user only
    payments = Payment.objects.filter(registration__user=request.user)
    return render(request, 'fee.html', {'payments': payments})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login_user') 
    else:
        form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})

@login_required
def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_panel')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'update_profile.html', {'form': form})