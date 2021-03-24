from django.shortcuts import render, redirect, HttpResponse

from .models import User

from utils.utils import hash

# Create your views here.
def register(request):
    context = {
        'error': ''
    }
    if request.method == 'GET':
        print(request.session.get('username', None))
        return render(request, 'register.html', context)

    elif request.method == 'POST':
        data = request.POST
        username = data['username']
        password = data['password']
        
        return render(request, 'register.html', context)

def login(request):
    context = {
        'error': ''
    }
    if request.method == 'GET':
        # request.session['username'] = 'anshit'
        return render(request, 'login.html', context)

    elif request.method == 'POST':
        data = request.POST
        print(data)
        username = data['username']
        password = data['password']
        print(username, password)
        users = User.objects.filter(username=username)
        if users.count() and users[0].password == hash(password):
            request.session['username'] = username
            return redirect('/')
        context['error'] = 'Incorrect username or password'
        return render(request, 'login.html', context)

def logout(request):
    request.session.pop('username', None)
    return redirect('/')

def checkUser(request, username):
    if User.objects.filter(username=username).count():
        return HttpResponse(1)
    return HttpResponse(0)