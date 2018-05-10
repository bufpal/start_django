# blog/admin.py
from django.contrib import admin
from .models import Post


# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']


    def content_size(self, post):
        return "{}".format(len(post.content))
    content_size.short_description="Content Length"