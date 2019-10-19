from django import forms
from . import Article, Comment

class ArticleModelForm(forms.Form):

    title = forms.CharField(min_length=1, max_length=20)
    content = forms.Textarea

    class Meta:
        model = Article
        fields = '__all__'

class CommentModelForm(forms.Form):

    content=forms.CharField(min_length=1, max_length=30)

    class Meta:
        model=Comment
        fields=('content',)
