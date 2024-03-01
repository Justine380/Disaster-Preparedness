from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CERTForm, EmergencyPlanForm, ResourceForm, CommunityForm
from .models import CERT, EmergencyPlan, Resource, Community

# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated: 
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user) 
            return redirect('home') 
        else:
            messages.error(request,'Username OR password does not exist')     

    context = {'page':page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')   


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'an error occurred during registration')

    return render(request, 'login_register.html', {'form':form}) 



def home(request):
    return render(request, 'home.html')


def drought(request):
    return render(request, 'Drought.html')


def floods(request):
    return render(request, 'floods.html')


def pandemics(request):
    return render(request, 'Pandemic.html')


def HomeFires(request):
    return render(request, 'Home fire.html')


def Get_intouch(request):
    return render(request, 'Get intouch with tech.html')


def safety(request):
    return render(request, 'safety skills.html')


def Fire_escape_plan(request):
    return render(request, 'Fire escape plan.html')


def get_involved(request):
    return render(request, 'Get Involved.html')


def about(request):
    return render(request, 'About Us.html')

def Contact(request):
    return render(request, 'Contact us.html')

