from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home-page'),
    path('delete-people/', delete, name='delete-people'),
    path('search/', search),
    path('lits/', lits, name="lits-page"),
    path('peoples/', peoples, name="peoples-page"),
    path('teachers/', teachers, name="teachers-page"),
    path('settings/', settings, name="settings-page"),
    path('trash/', trash, name="trash-page"),
]
