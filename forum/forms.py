from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content',  max_length=200, widget=forms.Textarea(attrs={'id': 'summernote', 'name': 'editordata'}))

    class Meta:
        model = Post
        fields = ('title', 'content')
