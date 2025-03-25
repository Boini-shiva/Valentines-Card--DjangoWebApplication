from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
   
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'SignUp Successfully ✅')
            return redirect('login')
        else:
            messages.error(request, 'Something Went Wrong ⚠️')
    else:
        signup_form = UserCreationForm()

    context = {
        'title': 'Welcome To Sign Up Page',
        'form': signup_form
    }

    return render(request, 'signup.html', context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, 'Both fields are required ⚠️')
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            
            if user.is_superuser:
                messages.success(request, 'Welcome Admin ✅')
                return redirect('admin:index')
            elif user.is_staff:
                messages.success(request, 'Welcome Staff ✅')
                return redirect('admin:index')
            else:
                messages.success(request, 'Login Successful ✅')
                return redirect('home')  # Redirect to home instead of signup
        else:
            messages.error(request, 'Invalid username or password ⚠️')

    return render(request,'login.html')


def log_out(request):
    logout(request)
    messages.success(request, "You have been logged out ✅")
    return redirect('login')
