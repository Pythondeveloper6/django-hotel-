from django.shortcuts import redirect, render
from .models import Post , Comments
from .forms import PostForm , CommentForm
from django.urls import reverse
from django.views.generic import ListView , DetailView , UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# Class Based Views
class PostList(LoginRequiredMixin ,ListView ):
    model = Post


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = ['title','content']
    success_url = '/blog/cbv'



# Function Based Views
# @login_required
def all_posts(request):
    ## logic
    all_posts = Post.objects.all()
    return render(request,'post/all_posts.html' ,{'posts':all_posts})


def single_post(request,id):
    #logic
    single_post = Post.objects.get(id=id)
    comments = Comments.objects.filter(post=single_post)

    if request.method == 'POST':
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            myform = commentform.save(commit=False)
            myform.author = request.user
            myform.post = single_post
            myform.save()
    
    else:
        commentform = CommentForm()


    return render(request,'post/single_post.html',{'post':single_post , 'comments':comments , 'commentform':commentform})


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



def post_edit(request,id):
    single_post = Post.objects.get(id=id)
    if request.method=='POST':  # new post to the blog
        form = PostForm(request.POST or None , request.FILES , instance=single_post)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:blog_list'))

    else:  # show form 
        form = PostForm(instance=single_post)
    return render(request,'post/new.html',{'form':form})
