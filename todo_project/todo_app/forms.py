from .models import task
from django import forms

class todoform(forms.ModelForm):
    class Meta:
        model=task
        fields=['title','description','date','priority']
       
def __init__(self, *args, **kwargs):
        super(todoform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})