from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home-page'),
    path('search/', search),
    path('lits/', lits, name="lits-page"),
    path('peoples/', peoples, name="peoples-page"),
    path('teachers/', teachers, name="teachers-page"),
    path('settings/', settings, name="settings-page"),
    path('trash/', trash, name="trash-page"),
    path('subjects/', subjects, name="subjects-page"),
    path('cources/', cources, name="cources-page"),
    
    
    path('delete-people/', deletePeople, name='delete-people'),
    path('delete-subject/', deleteSubject, name='delete-subject'),
]
