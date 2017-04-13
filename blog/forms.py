from django import forms
from blog.models import Article

# Create the form class.
class ArticleView(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user', 'title', 'text']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }

class ArticleEdit(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
