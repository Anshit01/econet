from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        pass

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        pass

def logout(request):
    return redirect('/')