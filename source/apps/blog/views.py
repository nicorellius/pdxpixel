from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader

# import class Post
from blog.models import Post


def index(request):
    # get the blog posts that are published
    posts = Post.objects.filter(published=True)
    # now return the rendered template
    return render(request, 'blog/index.html', {'posts': posts})


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def detail(request):
    return render(request, 'blog/detail.html')

def logout(request):
    return render(request, 'blog/logout.html')
