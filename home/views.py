from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')


def logout(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')


def search(request):
    if request.method == 'POST':
        pass
    return render(request, 'index.html')