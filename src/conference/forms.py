from django import forms
from .models import PaperRecord, AuthorRecord, ReviewPaperRecord


class authorRecordForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'placeholder': 'abcd@gmail.com', 'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$'}), max_length=50)
    mobileNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number'}), max_length=10)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country Name'}), max_length=50)
    organization = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Organization'}), max_length=100)
    url = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'URL'}), max_length=50)

    class Meta():
        model = AuthorRecord
        fields = ['name', 'email', 'mobileNumber', 'country', 'organization', 'url']


class paperRecordForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title*'}), required=True, max_length=100)
    abstract = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Abstract*'}), required=True, max_length=500)
    keywords = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Keywords'}), max_length=100)
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.pdf,.doc', 'style': "border:none"}),
                           required=True)

    class Meta():
        model = PaperRecord
        fields = ['title', 'abstract', 'keywords', 'file']


class reviewPaperForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comment'}), required=True)

    class Meta():
        model = ReviewPaperRecord
        fields = ['comment']
