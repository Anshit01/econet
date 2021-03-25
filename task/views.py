from django.shortcuts import render
from django.http import HttpResponse
from account.models import User
from task.models import TaskTodo

def taskHome(request):
    username = request.session.get('username', None)
    allTask = TaskTodo.objects.all()
    generalTasks = TaskTodo.objects.filter(taskType="G")
    weeklyTasks = TaskTodo.objects.filter(taskType="W")
    users = User.objects.filter(username=username)
    
    data = {
        'isLoggedin': True if username else False,
        'username': username,
        "allTasks":allTask,
        "generalTasks": generalTasks,
        "weeklyTasks" : weeklyTasks,
    }
    if users.count():
        data["user"] = users[0]

    return render(request, "task.html", data)
