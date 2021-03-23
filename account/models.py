from django.db import models
from djongo import models

from tasks.models import Task

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    imageURL = models.URLField(default="https://i.imgur.com/4zsBXBE.png")
    bio = models.TextField()

    #stats
    badge = models.CharField(max_length=100)
    points = models.IntegerField()

    tasksCompleted = models.ArrayReferenceField(
        to=Task,
        on_delete=models.CASCADE,
        blank=True
    )
    
    # posts: reverse reference

    def __str__(self):
        return str(self.id) + ' - ' + self.username + ' - ' + str(len(self.posts.all()))

class Post(models.Model):
    
    author = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    caption = models.TextField()
    imageURL = models.URLField()

    linkedTask = models.ForeignKey(
        to=Task,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True
    )
    #tags

    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.author)

