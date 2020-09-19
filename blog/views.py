from django.shortcuts import render
from .models import Post
from .forms import PostForm
# Create your views here.



def all_posts(request):
    ## logic
    all_posts = Post.objects.all()
    return render(request,'post/all_posts.html' ,{'posts':all_posts})


def single_post(request,id):
    #logic
    single_post = Post.objects.get(id=id)
    return render(request,'post/single_post.html',{'post':single_post})


def new_post(request):
    form = PostForm()
    return render(request,'post/new.html',{'form':form})