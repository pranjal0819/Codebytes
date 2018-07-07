from django import forms
from .models import paperRecord

class submitPaper(forms.ModelForm):
    name 		 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=True, max_length=40)
    email 		 = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'abcd@gmail.com','pattern':'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$'}), required=True, max_length=40)
    mobileNumber = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number'}), required=True, max_length=10)
    title 		 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}), required=True, max_length=50)
    body 	 	 = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body'}), required=True)
    file 		 = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept':'.pdf,.doc'}), required=True)

    class Meta():
        model = paperRecord
        fields = ['name','email','mobileNumber','title','body','file']
