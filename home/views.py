import json

import requests
from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotAllowed

from econet.config import config
from account.models import User, Post
from task.models import TaskTodo

# Create your views here.


def home(request):
    username = request.session.get('username', None)
    posts = Post.objects.all().reverse()
    alltasks = TaskTodo.objects.all()
    context = {
        'isLoggedin': True if username else False,
        'username': username,
        'posts': posts,
        'alltasks': alltasks

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
        data = dict(request.POST)
        print(data)
        linkedTask = None
        taskId = data['task'][0]
        if taskId:
            linkedTasks = TaskTodo.objects.filter(id=data['task'][0])
            if linkedTasks.count():
                linkedTask = linkedTasks[0]
        author = User.objects.filter(username=username)[0]
        newPost = Post(
            imageURL=data['imageURL'][0],
            author=author,
            caption=data['caption'][0],
            linkedTask=linkedTask
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
        author.save()
        post.save()
        return HttpResponse(1)
    return HttpResponse(0)
