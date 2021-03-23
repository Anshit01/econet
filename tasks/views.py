from django.shortcuts import render
from django.http import HttpResponse

from task.models import TaskTodo

def taskHome(request):
    generalTasks = TaskTodo.objects.filter(taskType="G")
    weeklyTasks = TaskTodo.objects.filter(taskType="W")

    data = {
        "generalTasks": generalTasks,
        "weeklyTasks" : weeklyTasks
    }

    return render(request, "task.html", data)
