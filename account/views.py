from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'GET':
        print(request.session.get('username', None))
        return render(request, 'register.html')

    elif request.method == 'POST':
        #TODO
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