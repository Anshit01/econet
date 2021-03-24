from django.shortcuts import render, redirect

from account.models import User, Post

# Create your views here. 
def user(request, username):
    loggedinUsername = request.session.get('username', None)
    posts = Post.objects.all().reverse()
    users = User.objects.filter(username=username)
    if users.count():
        context = {
            'user': users[0],
            'isLoggedin': True if loggedinUsername else False,
            'username': username,
            'posts': posts,
        }
        return render(request, 'profile.html', context)
    return redirect('/')