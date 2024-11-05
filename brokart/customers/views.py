from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import Custemer

# Create your views here.
def show_account(requst):
    context={}
    if requst.POST and "register" in requst.POST:
        context['register']=True
        try:
            username=requst.POST.get('username')
            email=requst.POST.get('email')
            address=requst.POST.get('address')
            phone=requst.POST.get('phone')
            password=requst.POST.get('password')
            #craete user account
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            #crate customer account
            Custemer.objects.create(
                user=user,
                phone=phone,
                address=address   
            )
            success_message="Account created"
            messages.success(requst,success_message)
        except Exception as e:
            error_message="Alredy you have an account"
            messages.error(requst,error_message)
    if requst.POST and "login" in requst.POST:
        context['register']=False
        username=requst.POST.get('username')
        password=requst.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(requst,user)
            return redirect('home')
        else:
            messages.error(requst,'invalid username and password')
 
    return render(requst,'account.html',context)

def sign_out(request):
    logout(request)
    return redirect('home')