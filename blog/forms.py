from django import forms
from blog.models import Article

# Create the form class.


class Article(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


class Search(forms.Form):
    keyword = forms.CharField(max_length=20, min_length=1, widget=forms.TextInput(attrs={'class': 'form-control'}))
