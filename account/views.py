from django.shortcuts import render, redirect, HttpResponse
import re

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
        print(data)
        username = str(data['username']).lower()
        password = data['password']
        print(username, password)
        if re.search('^[1-9a-z_]{3,30}$', username) is None:
            context['error'] = 'Invalid username'
            return render(request, 'register.html', context)
        if userExists(username):
            context['error'] = 'Username already exists'
            return render(request, 'register.html', context)
        newUser = User(
            username=username,
            password=hash(password),
            bio='Here goes your bio... Edit bio and profile picture from your profile page.',
            badge='Eco Newbie'
        )
        newUser.save()
        request.session['username'] = username
        return redirect('/')


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
    if userExists(username):
        return HttpResponse(1)
    return HttpResponse(0)


def userExists(username):
    if User.objects.filter(username=username).count():
        return True
    return False
