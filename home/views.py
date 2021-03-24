from django.shortcuts import render, HttpResponse

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
    users = User.objects.filter(username=username)
    if users.count():
        context["user"] = users[0]
    return render(request, 'home.html', context)

def likePost(request, id):
    username = request.session.get('username', None)
    posts = Post.objects.filter(id=id)
    if username and posts.count() > 0:
        post = posts[0]
        post.likes += 1
        author = post.author
        author.points += 1
        author.save()
        post.save()
        return HttpResponse(1)
    return HttpResponse(0)

