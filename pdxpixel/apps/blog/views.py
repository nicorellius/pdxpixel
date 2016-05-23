from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView

from taggit.models import Tag

from .models import Post


class TagMixin(object):

    def get_context_data(self, kwargs):

        context = super(TagMixin, self).get_context_data(kwargs)
        context['tags'] = Tag.objects.all()

        return context


class PostListView(ListView):

    model = Post
    context_object_name = 'posts'
    paginate_by = 5
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

        # tags = self.model.tag_aggregator(post)

        return render(request, self.template_name, {
            self.context_object_name: post
        })


class TagIndexView(ListView):

    template_name = 'tags.html'
    model = Post
    paginate_by = '10'
    context_object_name = 'posts'

    def get_queryset(self):

        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class TagListView(ListView):

    model = Tag
    context_object_name = 'tags'
    template_name = 'tags.html'
