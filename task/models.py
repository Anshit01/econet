from django.db import models

# Create your models here.

class TaskTodo(models.Model):
    name = models.CharField(max_length=200)
    worthPoints = models.IntegerField()
    taskType = models.CharField(max_length=1, choices=(("W", "Weekly"), ("G", "General")))

    def __str__(self):
        toRet = f"{self.name} - "
        if self.taskType == "W":
            toRet += "Weekly"
        else:
            toRet += "General"
        toRet += f" - {self.worthPoints}"
        return toRet