from django import forms
from .models import Article
from django.forms import ModelForm

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'category', 'title', 'abstract', 'key_word_1', 'key_word_2', 'key_word_3', 'body', 'image', 'status']
        
    # Customizing widgets for better UI
    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''})
        self.fields['abstract'].widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''})
        self.fields['body'].widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': ''})
        self.fields['image'].widget = forms.ClearableFileInput(attrs={'class': 'form-control'})
        self.fields['status'].widget = forms.Select(choices=Article.STATUS_CHOICES, attrs={'class': 'form-control'})
        self.fields['author'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(attrs={'class': 'form-control'})


