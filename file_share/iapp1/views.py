from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'iapp1/index.html')
    
def register(request):
    registered=False
    if request.method=='POST':
        uform=UserForm(data=request.POST)
        pform=UserProfileForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user=uform.save()
            user.set_password(user.password)
            user.save()
            profile=pform.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                print('fount it ')
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(uform.errors,pform.errors)
    else:
        uform=UserForm()
        pform=UserProfileForm()
    return render(request,'iapp1/registration.html',{'user_form':uform,'profile_form':pform,'register':registered})


def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')#HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account was inactive')
        else:
            return HttpResponse('Invalid Login Details given')
    else:
        return render(request,'iapp1/login.html',{})

@login_required
def userlogout(request):
    logout(request)
    return redirect('/')