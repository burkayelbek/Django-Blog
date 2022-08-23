from django import forms
from blog.models import PostModel


class UpdateTextFormModel(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ('slug', 'author')