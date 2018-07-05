from django import forms
from .models import paperRecord

class submitPaper(forms.ModelForm):

    class Meta():
        model = paperRecord
        fields = ['name','email','mobileNumber','title','body','file']
