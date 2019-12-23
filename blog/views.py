from django.shortcuts import render

# Create your views here.
from . models import Post
from django.views.generic import ListView

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'