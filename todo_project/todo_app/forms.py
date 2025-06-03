from .models import task
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model=task
        fields=['title','description','date','priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
        }
       
