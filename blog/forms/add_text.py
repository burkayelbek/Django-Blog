from django import forms
from blog.models import PostModel


class AddTextModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ('slug', 'author')