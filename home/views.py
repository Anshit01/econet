from django.shortcuts import render

# Create your views here.
def home(request):
    username = request.session.get('username', None)
    context = {
        'isLoggedin': True if username else False,
        'username': username,

    }
    return render(request, 'home.html', context)

