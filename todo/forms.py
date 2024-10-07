# todo/forms.py
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']
        widgets = {
            'description': SummernoteWidget(),
        }