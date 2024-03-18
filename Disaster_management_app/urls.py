from django.urls import path
from .views import *

urlpatterns = [
    path('', loginPage, name='login'),
    path('home/', home, name='home'),
    path('register/', registerPage, name='register'),
    path('drought/',drought, name='drought'),
    path('floods/',floods, name='floods'),
    path('pandemics/',pandemics, name='pandemics'),
    path('HomeFires/',HomeFires, name='HomeFires'),
    path('get_involved/',get_involved, name='get_involved'),
    path('Get_intouch/',Get_intouch, name='Get_intouch'),
    path('safety/',safety, name='safety'),
    path('Fire_escape_plan/',Fire_escape_plan, name='Fire_escape_plan'),
    path('about/',about, name='about'),
    path('Contact/',Contact, name='Contact'),
    path('adminpage/',adminpage, name='adminpage'),
    path('prediction/',prediction, name='prediction'),
    path('signout/',signout, name='signout')
]
