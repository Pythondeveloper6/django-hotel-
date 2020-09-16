from django.db import models
from django.utils import timezone

# Create your models here.

POST_TYPE = (
    ('DRAFT','DRAFT'),
    ('PUBLISHED' , 'PUBLISHED'),
)


class Post(models.Model):   # db table
    title = models.CharField(max_length=50 , unique=True)  # column
    content = models.TextField(max_length=2000 , null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    author_mail = models.EmailField(default='')
    type = models.CharField(choices=POST_TYPE , default='DRAFT',max_length=20)
    image = models.ImageField(upload_to='posts/')



    def __str__(self):
        return self.title

    # def __unicode__(self):
    #     return self.title