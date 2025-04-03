from django import forms
from .models import Task

#se utilizan asi en caso de escalabiliada y eficiencia, por si se usa muschas veces el form
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':3})
        }