from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in.
            login(request, user)
            return redirect('WorldTasks:worlds_list')  # Replace 'home' with the name of your home URL pattern.
    else:
        form = CustomUserCreationForm()
    return render(request, 'SignLog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('WorldTasks:worlds_list')  # Replace 'home' with the name of your home URL pattern.
        else:
            error_message = "Invalid login credentials."  # Add an error message
            return render(request, 'SignLog/login.html', {'error_message': error_message})
    return render(request, 'SignLog/login.html')

def logout_page(request):
    logout(request)
    return redirect('SignLog:login')
