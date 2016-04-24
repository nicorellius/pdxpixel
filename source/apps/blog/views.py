from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):

    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def index(request):

    posts = Post.objects.filter(published=True)

    return render(request, 'blog/index.html', {'posts': posts})


def get_post(request, slug):

    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post.html', {'post': post})


def post_detail(request, year, month, day, post):

    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        published__year=year,
        published__month=month,
        published__day=day
    )

    return render(request, 'blog/post/detail.html', {'post': post})


def logout(request):
    return render(request, 'blog/logout.html')
