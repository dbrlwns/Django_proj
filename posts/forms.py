from django import forms

from posts.models import Post

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

class PostForm(forms.ModelForm):
    images = MultipleFileField(required=False)

    class Meta:
        model = Post
        fields = ('title', 'content')
