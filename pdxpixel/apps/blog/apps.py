from django.apps import AppConfig
from watson import search as watson


class BlogConfig(AppConfig):

    name = 'apps.blog'

    def ready(self):

        post = self.get_model('Post')
        watson.register(post)
