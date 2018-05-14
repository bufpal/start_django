# blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Tag


# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status', 'content_size', 'created_at', 'updated_at']
    actions = ['make_draft', 'make_published']


    def content_size(self, post):
        return "{}".format(len(post.content))
    content_size.short_description="Content Length"


    def make_draft(self, request, queryset):
        query_count = queryset.update(status='d')
        self.message_user(request, 'Changed {} items status to Draft'.format(query_count))
    make_draft.short_description="change checked to 'draft'"


    def make_published(self, request, queryset):
        query_count = queryset.update(status='p')
        self.message_user(request, 'Changed {} item status to Published'.format(query_count))
    make_published.short_description="change checked to 'published'"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_id', 'author', 'message']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag',]