from django.apps import AppConfig
from watson import search as watson


class FlatpageConfig(AppConfig):

    name = 'django.contrib.flatpages'

    def ready(self):

        flatpage = self.get_model('FlatPage')
        watson.register(flatpage)
