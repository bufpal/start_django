from django.views.generic import ListView
from .models import Post


post_list = ListView.as_view(model=Post, paginate_by=10)