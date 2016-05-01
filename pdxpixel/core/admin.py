from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.utils.translation import ugettext_lazy as _


class ExtendedFlatPageAdmin(FlatPageAdmin):

    form = FlatpageForm

    fieldsets = (
        (None, {'fields': ('url', 'title', 'description', 'content', 'sites')}),
        (_('Advanced options'), {
            'classes': ('collapse',),
            'fields': (
                'registration_required',
                'enable_comments',
                'template_name',
            ),
        }),
    )

    list_display = ('url', 'title', 'description')


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)