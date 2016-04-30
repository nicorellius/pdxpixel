from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.forms import FlatpageForm
from django.utils.translation import ugettext_lazy as _

# from .forms import ExtendedFlatPageForm


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

# ===========================================================

# from django.contrib.flatpages.models import FlatPage
# from django.contrib.flatpages.forms import forms
#
# # from .models import ExtendedFlatPage
#
#
# class ExtendedFlatPageForm(forms.ModelForm):
#
#     description = forms.CharField(max_length=500)
#
#     class Meta:
#         model = FlatPage
#         fields = '__all__'
#
#     def save(self, commit=True):
#
#         description = self.cleaned_data.get('description', None)
#         self.description = description
#
#         return super(ExtendedFlatPageForm, self).save(commit=commit)
#
#
# from django.db import models
#
# from django.contrib.flatpages.models import FlatPage
#
#
# class ExtendedFlatPage(FlatPage):
#
#     description = models.CharField(max_length=500)
