from django.db import models
from djongo import models
from datetime import datetime

from task.models import TaskTodo

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=100)
    imageURL = models.URLField(default="https://i.imgur.com/4zsBXBE.png")
    bio = models.TextField()
    joinedOn = models.DateTimeField(default=datetime.now)

    #stats
    badge = models.CharField(max_length=100)
    points = models.IntegerField()

    tasksCompleted = models.ArrayReferenceField(
        to=TaskTodo,
        on_delete=models.CASCADE,
        blank=True
    )
    
    # posts: reverse reference

    def __str__(self):
        return self.username + ' - ' + str(len(self.posts.all()))

class Post(models.Model):
    
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    caption = models.TextField()
    imageURL = models.URLField()
    postedOn = models.DateTimeField(default=datetime.now)

    linkedTask = models.ForeignKey(
        to=TaskTodo,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True
    )
    #tags

    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.author)

