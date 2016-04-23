from django.contrib import admin
from django import forms
from blog.models import Post
from pagedown.widgets import PagedownWidget, AdminPagedownWidget
from django.db import models

class PostAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['title', 'description']
    
    # fields to filter the change list with
    list_filter = ['published', 'pub_date']
    
    # fields to search in change list
    search_fields = ['title', 'description', 'content']
    
    # enable the date drill down on change list
    date_hierarchy = 'pub_date'
    
    # enable the save buttons on top on change form
    save_on_top = True
    
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
    
    # pagedown override for admin posts
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Post, PostAdmin)
