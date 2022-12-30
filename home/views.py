from django.shortcuts import render, redirect
from .models import *


def home(request):
    context = {'page_name': 'home'}
    return render(request, 'home-page.html', context=context)


def lits(request):
    context = {'page_name': 'lits'}
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

            new_people = People.objects.create(
                full_name=full_name, birthday=birthday, phone=phone)

    if q:
        peoples = People.objects.filter(full_name__icontains=q)

    context = {'page_name': 'peoples', 'peoples': peoples,
               'subjects': subjects, 'courses': courses, }
    return render(request, 'peoples.html', context=context)


def teachers(request):
    context = {'page_name': 'teachers'}
    return render(request, 'teachers.html', context=context)


def settings(request):
    context = {'page_name': 'settings'}
    return render(request, 'settings.html', context=context)


def trash(request):
    context = {'page_name': 'trash'}
    return render(request, 'trash.html', context=context)


def subjects(request):
    subjects = Subject.objects.all()
    
    if request.method == 'POST':
        if request.POST.get('type'):
            id = request.POST.get('id')
            name = request.POST.get('name')
            
            print(name, id)
            
            subject = Subject.objects.get(id=id)
            subject.name = name
            subject.save()
            
            
        else:
            name = request.POST.get('name')
        
            newSubject = Subject.objects.create(name=name)


    
    context = {'page_name': 'subjects', 'subjects' : subjects}
    return render(request, 'subjects.html', context=context)


def cources(request):
    context = {'page_name': 'cources'}
    return render(request, 'cources.html', context=context)


def search(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')


def deletePeople(request):
    id = request.GET.get('id')
    People.objects.get(pk=id).delete()

    return redirect(request.META.get('HTTP_REFERER'))


def deleteSubject(request):
    id = request.GET.get('id')
    Subject.objects.get(pk=id).delete()

    return redirect(request.META.get('HTTP_REFERER'))
