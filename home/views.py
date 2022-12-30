from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login as lgn, logout as lgt, authenticate
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(request, username=username, password=password)
        
        if user:
            lgn(request=request, user=user)
            
            return redirect('home-page')


    return render(request, 'login.html')


@login_required(login_url='login-page')
def home(request):
    context = {'page_name': 'home'}
    return render(request, 'home-page.html', context=context)


@login_required(login_url='login-page')
def lits(request):
    context = {'page_name': 'lits'}
    return render(request, 'lits.html', context=context)


@login_required(login_url='login-page')
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


@login_required(login_url='login-page')
def teachers(request):
    context = {'page_name': 'teachers'}
    return render(request, 'teachers.html', context=context)


@login_required(login_url='login-page')
def settings(request):
    context = {'page_name': 'settings'}
    return render(request, 'settings.html', context=context)


@login_required(login_url='login-page')
def trash(request):
    context = {'page_name': 'trash'}
    return render(request, 'trash.html', context=context)


@login_required(login_url='login-page')
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

    context = {'page_name': 'subjects', 'subjects': subjects}
    return render(request, 'subjects.html', context=context)


@login_required(login_url='login-page')
def cources(request):
    context = {'page_name': 'cources'}
    return render(request, 'cources.html', context=context)


@login_required(login_url='login-page')
def deletePeople(request):
    id = request.GET.get('id')
    People.objects.get(pk=id).delete()

    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login-page')
def deleteSubject(request):
    id = request.GET.get('id')
    Subject.objects.get(pk=id).delete()

    return redirect(request.META.get('HTTP_REFERER'))


def logout(request):
    lgt(request)
    
    return redirect('login-page')
    