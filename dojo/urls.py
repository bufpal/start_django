from django.conf.urls import url
from dojo import views

urlpatterns = [
    url('^$', views.post_list)
]