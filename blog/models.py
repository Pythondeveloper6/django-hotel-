from django.db import models

# Create your models here.


class Post(models.Model):   # db table
    title = models.CharField(max_length=50)  # column
    content = models.TextField(max_length=2000)


    def __str__(self):
        return self.title
