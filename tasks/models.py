from django.db import models

from utils.utils import generateUUID
# Create your models here.


# class TaskTodo(models.Model):
#     # id = models.CharField(max_length=100, default=generateUUID, primary_key=True)
#     name = models.CharField(max_length=200)
#     worthPoints = models.IntegerField()
#     taskType = models.CharField(max_length=1, choices=(
#             ("W", "Weekly"), ("G", "General")
#         )
#     )

#     # def __str__(self):
#     #     return name

# class TaskTodo(models.Model):
#     name = models.CharField(max_length=200)
#     worthPoints = models.IntegerField()
#     taskType = models.CharField(max_length=1, choices=(("W", "Weekly"), ("G", "General")))
