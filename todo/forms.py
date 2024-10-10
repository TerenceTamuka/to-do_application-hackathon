# todo/forms.py
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import TodoItem

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'due_date', 'description']
        widgets = {
            'due_date': forms.widgets.DateTimeInput(attrs={'type': 'datetime-local'}),
            'description': SummernoteWidget(),
        }

    # def clean_due_date(self):
    #     due_date = self.cleaned_data.get('due_date')
    #     if due_date and due_date < timezone.now():
    #         raise forms.ValidationError("The due date cannot be in the past.")
    #     return due_date