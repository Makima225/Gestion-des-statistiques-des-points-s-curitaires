from django import forms
from .models import *

class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_of_event': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'unit':forms.Select(attrs={'class': 'form-select'}),
            'locality':forms.Select(attrs={'class': 'form-select'}),
            'category_event':forms.Select(attrs={'class': 'form-select'}),
            'bilan':forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


