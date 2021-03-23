from django.shortcuts import render, redirect

from account.models import User, Post

# Create your views here.
def user(request, username):
    username = request.session.get('username', None)
    users = User.objects.filter(username=username)
    if users.count():
        context = {
            'user': users[0],
            'isLoggedin': True if username else False,
            'username': username,
        }
        return render(request, 'profile.html', context)
    return redirect('/')