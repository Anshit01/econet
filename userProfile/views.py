from django.shortcuts import render, redirect

from account.models import User, Post
from utils.utils import getUserPointsAndRank

# Create your views here. 
def user(request, username):
    loggedinUsername = request.session.get('username', None)
    posts = Post.objects.filter(author=username).order_by('-id')
    users = User.objects.filter(username=username)
    points, rank = getUserPointsAndRank(username)
    if users.count():
        context = {
            'user': users[0],
            'isLoggedin': True if loggedinUsername else False,
            'username': loggedinUsername,
            'posts': posts,
            'tasksCompleted': users[0].tasksCompleted.all(),
            'points': points,
            'rank': rank
        }
        return render(request, 'profile.html', context)
    return redirect('/')
