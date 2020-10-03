from django.urls import path
from .views import profile , profile_edit


app_name = 'accounts'

urlpatterns = [
    path('profile/edit', profile_edit)
]
