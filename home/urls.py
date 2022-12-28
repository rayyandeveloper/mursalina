from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login),
    path('register/', register),
    path('logout/', logout),
    path('search/', search),
]


