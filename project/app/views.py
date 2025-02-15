from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse('hello')
def page(request):
    return render(request,'base.html')
def profile1(request):
    return render(request,'profile1.html')
def Finished_books(request):
    return render(request,'Finished_books.html')
def Unfinished_books(request):
    return render(request,'Unfinished_books.html')
def Course(request):
    return render(request,'Course.html')
def general(request):
    return render(request,'General_books.html')
def login(request):
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')
        
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect('base.html')  # Replace 'home' with your homepage URL name
    return render(request, 'register.html')

@login_required
def profile(request):
    user = request.user  # Access logged-in user details
    return render(request, 'profile.html', {'user': user})