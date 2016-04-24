import datetime

from django.utils import timezone
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, unique_for_date='published')
    author = models.ForeignKey(User, related_name='blog_posts')
    description = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.published >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.published.year,
            self.published.strftime('%m'),
            self.published.strftime('%d'),
            self.slug
        ])
