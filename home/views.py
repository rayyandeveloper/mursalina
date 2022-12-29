from django.shortcuts import render
from .models import *

def home(request):
    context = {'page_name' : 'home'}
    return render(request, 'home-page.html', context=context)





def lits(request):
    context = {'page_name' : 'lits'}
    return render(request, 'lits.html', context=context)




def peoples(request):


    peoples = People.objects.all()
    courses = Course.objects.all()
    subjects = Subject.objects.all()

    context = {'page_name' : 'peoples', 'peoples' : peoples, 'subjects' : subjects, 'courses' : courses,}
    return render(request, 'peoples.html', context=context)




def teachers(request):
    context = {'page_name' : 'teachers'}
    return render(request, 'teachers.html', context=context)




def settings(request):
    context = {'page_name' : 'settings'}
    return render(request, 'settings.html', context=context)




def trash(request):
    context = {'page_name' : 'trash'}
    return render(request, 'trash.html', context=context)



def search(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')