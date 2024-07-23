from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('admin:index')
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
                    return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'index.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('admin:index')
    else:

        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account created for ' +user)
               return redirect('index')
        context = {'form':form}
        return render(request, 'register.html', context)



