from django import forms
from blog.models import Article

# Create the form class.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user', 'title', 'text']
