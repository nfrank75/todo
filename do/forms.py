from django import forms
from django.forms import ModelForm

from .models import Todo

class TodoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Todo
        fields=(
            'name',
            'description',
            'File',
            'complete'
             )