from . models import todo
from django import forms

class todo_form(forms.ModelForm):
    class Meta:
        model=todo
        fields=['name','priority','date']