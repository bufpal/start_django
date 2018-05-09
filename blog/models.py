from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Subject", help_text="input title, max 100")
    content = models.TextField(verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
