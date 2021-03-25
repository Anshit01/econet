import json

from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotAllowed

from econet.config import config
from account.models import User, Post
from task.models import TaskTodo

from utils.utils import updateUserPoints

# Create your views here.


def home(request):
    username = request.session.get('username', None)
    posts = Post.objects.all().order_by('-id')
    alltasks = TaskTodo.objects.all()
    weeklyTasks = TaskTodo.objects.filter(taskType='W')
    generalTasks = TaskTodo.objects.filter(taskType='G')
    context = {
        'isLoggedin': True if username else False,
        'username': username,
        'posts': posts,
        'alltasks': alltasks,
        'weeklyTasks': weeklyTasks,
        'generalTasks': generalTasks

    }
    users = User.objects.filter(username=username)
    if users.count():
        context["user"] = users[0]
    return render(request, 'home.html', context)

def getPost(request):
    id = request.GET["id"]
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Not Found")

    return render(request, "post.html", context={"post":post})

def newPost(request):
    if request.method == "POST":
        username = request.session.get('username', None)
        print("Got a new post")
        data = request.POST
        print(data)
        linkedTask = None
        taskId = data['task']
        author = User.objects.filter(username=username)[0]
        if taskId:
            linkedTasks = TaskTodo.objects.filter(id=data['task'])
            if linkedTasks.count():
                linkedTask = linkedTasks[0]
                points = linkedTask.worthPoints
                author.points += points
                updateUserPoints(username, points)
                author.tasksCompleted.add(linkedTask)
        newPost = Post(
            imageURL=data['imageURL'],
            author=author,
            caption=data['caption'],
            linkedTask=linkedTask,
        )
        newPost.save()
        return HttpResponse(1)
    return HttpResponseNotAllowed(['POST'])

def likePost(request, id):
    username = request.session.get('username', None)
    posts = Post.objects.filter(id=id)
    if username and posts.count() > 0:
        post = posts[0]
        post.likes += 1
        author = post.author
        author.points += 1
        updateUserPoints(username, 1)
        author.save()
        post.save()
        return HttpResponse(1)
    return HttpResponse(0)
