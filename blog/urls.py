from django.urls import path
from blog.views import all_posts , single_post


urlpatterns = [
    path('' , all_posts),
    path('<int:id>',single_post)
]