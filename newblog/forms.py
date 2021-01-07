from .models import Post
from django import forms

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','title_tag','blog_category','author','body','header_image')

        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'blog_category' : forms.Select(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            # 'header_image':forms.ImageField(attrs={'class':'form-control'}),
            
        }

class FormEdit(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','title_tag','body')

        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }