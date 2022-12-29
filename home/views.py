from django.shortcuts import render, redirect
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

    q = request.GET.get('q')

    if request.method == 'POST':
        if request.POST.get('type'):
            id = request.POST.get('id')
            full_name = request.POST.get('full-name')
            birthday = request.POST.get('birthday')
            phone = request.POST.get('phone')
            
            people = People.objects.get(pk=id)
            
            people.full_name = full_name
            people.birthday = birthday
            people.phone = phone
            people.save()
        else:
            data = request.POST
            full_name = data['full-name']
            birthday = data['birthday']
            phone = data['phone']

            new_people = People.objects.create(full_name=full_name, birthday=birthday, phone=phone)
            

    if q:
        peoples = People.objects.filter(full_name__icontains=q)

    
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


def delete(request):
    id = request.GET.get('id')
    people = People.objects.get(pk=id).delete()
    
    return redirect(request.META.get('HTTP_REFERER'))