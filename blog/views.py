from django.shortcuts import render
from django.views import generic
from .models import Post


# from django.http import HttpResponse
# def blog_home(request):
#     return HttpResponse("Hello, blog!")

class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=4)
    queryset = Post.objects.filter(status=1)

    template_name = "post_list.html"
