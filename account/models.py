from django.db import models

from tasks.models import Task

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    imageURL = models.URLField()
    bio = models.TextField()

    #stats
    badge = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField()

    tasksCompleted = models.ArrayReferenceField(
        to=Task,
        on_delete=models.CASCADE
    )
    
    posts = models.ArrayReferenceField(
        to=Post,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username

class Post(models.Model):
    
    caption = models.TextField()
    imageURL = models.URLField()
    
    linkedTask = models.ForeignKey(
        to=Task,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

