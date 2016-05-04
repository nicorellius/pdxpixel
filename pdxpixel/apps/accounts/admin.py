from django.contrib import admin


from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = [
        'user', 'name', 'organization',
        'title', 'phone', 'location', 'website',
    ]

    # fields to filter the change list with
    list_filter = ['user', 'organization']

    # fields to search in change list
    search_fields = ['user', 'organization', 'title']

    # enable the date drill down on change list
    date_hierarchy = 'created'

    # enable the save buttons on top on change form
    save_on_top = True

    # pre-populate the slug from the title - big time saver!
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(UserProfile, UserProfileAdmin)
