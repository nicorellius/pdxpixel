from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from .models import Post


class PostListView(ListView):

    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'


class GetPostDetailView(View):

    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'

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
