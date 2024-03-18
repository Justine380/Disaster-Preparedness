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
from django.contrib.auth.models import Group
from .decorator import users_responsibility
from rest_framework.response import Response
from django.template.loader import render_to_string
from .models import EnvironmentalFactors


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
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


def prediction(request):
    if request.method == 'POST':
        # Get user inputs
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        dewpoint = float(request.POST.get('dewpoint'))
        land_surface_temperature = float(request.POST.get('Land'))
        low_atmospheric_pressure = float(request.POST.get('Low atmospheric pressure'))
        streamflow_river_discharge = float(request.POST.get('Streamflow and River discharge'))
        unhealthy_vegetation = float(request.POST.get('Unhealthy Vegetation'))
        smoking_indoors = float(request.POST.get('smoking indoors'))
        smoke_detectors = float(request.POST.get('Smoke Detectors'))
        fire_extinguishers = float(request.POST.get('Fire Extinguishers'))
        open_flame = float(request.POST.get('Open flame'))
        high_transmission_rate = float(request.POST.get('High Transmission rate'))
        high_hospitalized_rate = float(request.POST.get('High hospitalized rate'))
        high_number_of_cases = float(request.POST.get('High Number of cases'))
        
        #query the database 
        environmental_factors, created = EnvironmentalFactors.objects.get_or_create()
        environmental_factors.temperature = temperature
        environmental_factors.humidity = humidity
        environmental_factors.dewpoint = dewpoint
        environmental_factors.land_surface_temperature = land_surface_temperature
        environmental_factors.low_atmospheric_pressure = low_atmospheric_pressure
        environmental_factors.streamflow_river_discharge = streamflow_river_discharge
        environmental_factors.unhealthy_vegetation = unhealthy_vegetation
        environmental_factors.smoking_indoors = smoking_indoors
        environmental_factors.smoke_detectors = smoke_detectors
        environmental_factors.fire_extinguishers = fire_extinguishers
        environmental_factors.open_flame = open_flame
        environmental_factors.high_transmission_rate = high_transmission_rate
        environmental_factors.high_hospitalized_rate = high_hospitalized_rate
        environmental_factors.high_number_of_cases = high_number_of_cases
        environmental_factors.save()
    return render(request, 'response.html')
        
        
       

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group=Group.objects.get(name='clients')
            user.groups.add(group)
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


@users_responsibility(user_roles=['admin'])
def adminpage(request):
    return render(request, 'adminpage.html')


def signout(request):
    logout(request)
    return redirect('login')