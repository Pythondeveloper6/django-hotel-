from django.urls import path
from blog.views import all_posts , single_post



app_name='blog'

urlpatterns = [
    path('' , all_posts , name='blog_list'),
    path('<int:id>',single_post,name='blog_detail')
]