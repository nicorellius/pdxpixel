# from django.shortcuts import render

from watson.views import BaseListView


class SearchView(BaseListView):

    template_name = 'base_search.html'
