from django.contrib import admin
from .models import GameUser, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(GameUser)
class GameUserAdmin(admin.ModelAdmin):
    pass