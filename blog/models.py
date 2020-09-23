from django.db import models
from django.utils import timezone
from django.urls import reverse

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


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posties'
        ordering = ('-active',)
        # db_table = ''


    def __str__(self):
        return self.title

    def get_read_time(self):
        pass

    def get_absolute_url(self):
        return reverse("blog:cbv_detail", kwargs={"pk": self.id})
    


class Comments(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    # post = models.ManyToManyField(Post)
    text = models.TextField(max_length=200)


    def __str__(self):
        return str(self.post)