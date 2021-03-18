from django.shortcuts import render, redirect, HttpResponse, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Posts
from .forms import *
from django.views.generic.edit import UpdateView
import datetime as dt
from .decorators import unregistered_user, allowed_users, admin_only
from django.contrib.auth.models import Group
# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            group_user = form.save()

            group = Group.objects.get(name='auth_user')
            group_user.groups.add(group)

            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password1=form.cleaned_data['password1']
            recipient=User(username=username,email=email)
            try:
                send_welcome_email(username,email)
                messages.success(request, f'Account has been created successfully!')
            except:
                print('error')
            return redirect('login') 
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'registration/login.html')

@login_required
def AdminDashboard(request):
    users = Posts.objects.all()
    return render(request, 'index2.html')


def DoctorsDashboard(request):
    return render(request, 'doctor-list.html')