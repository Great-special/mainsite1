from django.shortcuts import render, redirect
from .models import User_Details
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.


def register(request):
    if request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone no']
        address = request.POST['address']
        fullname = str(last_name) + str(' ') + str(first_name)

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Already Exist!')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exist!')
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email, password=password)
            user.save()

            userD = User_Details(full_name=fullname, address=address, phone_no=phone_no, email=email)
            userD.save()
            messages.success(request, 'User Registered')
            return redirect('/')
    else:
        return render(request, 'register.html')


def log_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user != None:
            auth.login(request, user)
            messages.success(request, 'Logged in')
            return redirect('/')
        else:
            messages.error(request, 'Log In Details Incorrect')
            return redirect('log_in')
    else:
        return render(request, 'log in.html')


def log_out(request):
    auth.logout(request)
    return redirect('/')