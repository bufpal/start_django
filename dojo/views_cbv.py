import os
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View, TemplateView

class PostListView1(View):
    def get(self, request):
        name = "Ben"
        html = self.get_string().format(name=name)
        return HttpResponse(html)
    

    def get_string(self):
        return """
        <h1>Hello {name}</h1>
        <p> It's just beginning </p>
        """

post_list1 = PostListView1.as_view()



class PostListView2(TemplateView):
    template_name = "dojo/post_list2.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = "Ben"
        return context

post_list2 = PostListView2.as_view()



class PostListView3(View):
    def get(self, request):
        html = JsonResponse(self.get_data(), json_dumps_params={"ensure_ascii": False})    
        return html

    def get_data(self):
        return {
            "items": ["python", "django", "data", "algorithm"],
            "message": "road to python and django developer",
        }

post_list3 = PostListView3.as_view()



class download_excel(View):
    pass