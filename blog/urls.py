from django.urls import path
from blog.views import all_posts , single_post , new_post



app_name='blog'

urlpatterns = [
    path('' , all_posts , name='blog_list'),
    path('new' , new_post , name='new_post'),
    path('<int:id>',single_post,name='blog_detail')
]