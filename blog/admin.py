# blog/admin.py
from django.contrib import admin
from .models import Post, Comment, Tag


# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status', 'content_size', 'created_at', 'updated_at', 'tag_list', 'comment_list']
    actions = ['make_draft', 'make_published']

    def tag_list(self, post):
        tags = post.tag_set.all()
        return '/ '.join(tag.tag for tag in tags)

    
    def comment_list(self, post):
        comments = post.comment_set.all()
        return '/'.join(comment.message for comment in comments)


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set', 'comment_set')


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
    list_display = ['id', 'post_id', 'author', 'message', 'post_content_length']
    list_select_related = ['post']
    
    def post_content_length(self, comment):
        return len(comment.post.content)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
