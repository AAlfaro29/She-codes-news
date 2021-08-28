from django import forms
from django.forms import ModelForm
from .models import NewsStory
from django.forms import TextInput, EmailInput, DateInput

    
class StoryForm(ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title', 'style': 'width: 300px;'}))
    # pub_date = forms.DateField(widget=forms.DateInput(attrs={'placeholder' :'Pub date', 'style': 'width: 300px;'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Content', 'style': 'width: 300px;'}))
    img_url = forms.CharField(widget=forms.TextInput(attrs={'placeholder' :'Img url', 'style': 'width: 300px;'}))


    class Meta:
        model = NewsStory
        fields = ['title','pub_date', 'content', 'img_url']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Selecta date','type':'date'}),
        }
    