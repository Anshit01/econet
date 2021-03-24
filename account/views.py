from django.shortcuts import render, redirect, HttpResponse

from .models import User

# Create your views here.
def register(request):
    if request.method == 'GET':
        print(request.session.get('username', None))
        return render(request, 'register.html')

    elif request.method == 'POST':
        password = "ProvideFrom"
        pass

def login(request):
    if request.method == 'GET':
        request.session['username'] = 'anshit'
        return render(request, 'login.html')

    elif request.method == 'POST':
        #TODO
        pass

def logout(request):
    request.session.pop('username', None)
    #TODO handle logout
    return redirect('/')    

def checkUser(request, username):
    if User.objects.filter(username=username).count():
        return HttpResponse(1)
    return HttpResponse(0)