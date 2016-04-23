from django import forms
from django.contrib.comments.forms import CommentForm
from pagedown.models import AdminPagedownWidget
from pagedown.widgets import AdminPagedownWidget 

class CommentFormWithPagedown(CommentForm):
    comment = forms.CharField(max_length=500)

    def get_comment_model(self):
        # Use our custom comment model instead of the built-in one.
        return AdminPagedownWidget

    def get_comment_create_data(self):
        # Use the data of the superclass, and add in the title field
        data = super(CommentFormWithPagedown, self).get_comment_create_data()
        data['comment'] = self.cleaned_data['comment']
        return data