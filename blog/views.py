from django.shortcuts import render
from .models import Post
# Create your views here.



def all_posts(request):
    ## logic
    all_posts = Post.objects.all()
    return render(request,'post/all_posts.html' ,{'posts':all_posts})


def single_post(request,id):
    #logic
    single_post = Post.objects.get(id=id)
    return render(request,'post/single_post.html',{'post':single_post})