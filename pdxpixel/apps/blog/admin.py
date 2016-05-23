from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget


from .models import Post


class PostAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    # fields display on change list
    list_display = ['title', 'description', 'status']
    
    # fields to filter the change list with
    list_filter = ['status', 'published']
    
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    
    # enable the date drill down on change list
    date_hierarchy = 'published'
    
    # enable the save buttons on top on change form
    save_on_top = True
    
    # pre-populate the slug from the title - big time saver!
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
