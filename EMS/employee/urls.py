from django.urls import path
from .views import *

urlpatterns = [
    path('homee/', homeview, name = 'home'),
    
]
