from django.shortcuts import render
from django.http import HttpResponse

from tasks.models import Task

def taskHome(request):
    generalTasks = Task.objects.filter(taskType="G")
    weeklyTasks = Task.objects.filter(taskType="W")

    data = {
        "generalTasks": generalTasks,
        "weeklyTasks" : weeklyTasks
    }

    return render(request, "task.html", data)
