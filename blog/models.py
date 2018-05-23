import re
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.\d+),([+-]?\d+\.\d+)$', value):
        raise ValidationError('Invalid LngLat Type')
    

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100, verbose_name="Subject", help_text="input title, max 100")
    content = models.TextField(verbose_name="Content")
    photo = models.ImageField(blank=True)
    tag = models.CharField(max_length=50, blank=True, help_text="write tags")
    lnglat = models.CharField(max_length=30,
        validators=[lnglat_validator],
        help_text="\"longtitude,latitude\" type",
        blank=True
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set = models.ManyToManyField('Tag', blank=True)
    ip = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-id']

    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args = [self.id])    


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag