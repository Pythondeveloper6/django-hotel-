from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
from django.urls import reverse
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
    print('In View')
    if request.method=='POST':  # new post to the blog
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:blog_list'))

    else:  # show form 
        form = PostForm()
    return render(request,'post/new.html',{'form':form})