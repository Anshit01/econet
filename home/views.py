import json

import requests
from django.shortcuts import render
from django.http import HttpResponse

from econet.config import config
from account.models import User, Post
from task.models import TaskTodo

# Create your views here.


def home(request):
    username = request.session.get('username', None)
    posts = Post.objects.all()
    alltasks = TaskTodo.objects.all()
    context = {
        'isLoggedin': True if username else False,
        'username': username,
        'posts': posts,
        'alltasks': alltasks

    }
    return render(request, 'home.html', context)


def getPost(request):
    id = request.GET["id"]
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Not Found")

    return render(request, "post.html", context={"post":post})

def newPost(request):
    url = "https://api.imgur.com/3/image"
    payload={'image': 'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'}
    files=[
    ]
    headers = {
    'Authorization': f'Client-ID {config["IMGUR_CLIENT_ID"]}'
    }
    res = requests.request("POST", url, headers=headers, data=payload, files=files)
    response = json.loads(res.text)
    if response["success"]:
        # Image Uploaded
        imageUploadedLink = response["data"]["link"]
        imageDeleteHash = response["data"]["deletehash"]
    else:
        # Image Upload Failed
        pass
    return HttpResponse(str(vars(request.POST)))
