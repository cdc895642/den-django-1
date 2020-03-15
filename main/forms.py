from django import forms
from .models import Post
class AppImg(forms.ModelForm):
    class Meta:
        model=Post
        fields=['img']

class Creating(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=Post
        fields=['title','text','category']



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','img' )