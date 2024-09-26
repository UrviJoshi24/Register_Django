from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password

def home(request):
    return render(request, 'postgresql/home.html')

def login(request):
    if request.method == 'POST':
        useremail = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(useremail=useremail)
            
            # Use check_password to verify hashed passwords
            if check_password(password, user.password):
                request.session['useremail'] = user.useremail
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')
        
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('login')

    return render(request, 'postgresql/login.html')

def register(request):
    if request.method == 'POST':
        # Add registration logic here
        username = request.POST['username']
        password = request.POST['password']
        useremail = request.POST['email']
        if User.objects.filter(useremail=useremail).exists():
            messages.info(request,'User email is taken')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username is taken')
            return redirect('register')
        else:
            user = User.objects.create(username=username,password=password,useremail=useremail)
            user.save()
            print("user created")
            return redirect('login')  # After successful registration, redirect to login page
    return render(request, 'postgresql/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')
