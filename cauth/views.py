from django.shortcuts import render

# Create your views here.

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

