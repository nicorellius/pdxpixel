from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from .models import Post


class PostListView(ListView):

    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# class GetPostView(View):
#
#     model = Post
#     # context_object_name = 'post'
#     template_name = 'blog/post.html'
#
#     def get(self, request, slug):
#
#         post = get_object_or_404(Post, slug=slug)
#
#         return render(request, self.template_name, {'post': post})


# def get_post(request, slug):
#
#     post = get_object_or_404(Post, slug=slug)
#
#     return render(request, 'blog/post.html', {'post': post})


class GetPostDetailView(View):

    model = Post
    context_object_name = 'post'
    template_name = 'blog/post/detail.html'

    def get(self, request, year, month, day, entry):

        post = get_object_or_404(
            Post,
            slug=entry,
            status='published',
            published__year=year,
            published__month=month,
            published__day=day
        )

        return render(request, self.template_name, {self.context_object_name: post})


# def post_detail(request, year, month, day, post):
#
#     post = get_object_or_404(
#         Post,
#         slug=post,
#         status='published',
#         published__year=year,
#         published__month=month,
#         published__day=day
#     )
#
#     return render(request, 'blog/post/detail.html', {'post': post})
