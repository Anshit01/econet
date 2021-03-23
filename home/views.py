from django.shortcuts import render

from account.models import User, Post
from task.models import TaskTodo

# Create your views here.
def home(request):
    username = request.session.get('username', None)
    posts = Post.objects.all()
    context = {
        'isLoggedin': True if username else False,
        'username': username,
        'posts': posts,
        
    }
    return render(request, 'home.html', context)

