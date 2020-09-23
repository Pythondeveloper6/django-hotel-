from django.contrib import admin

# Register your models here.
from .models import Post , Comments


class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'type', 'active']
    list_filter = ['type','active']
    search_fields = ['title','content']




admin.site.register(Post , PostAdmin)


admin.site.register(Comments)