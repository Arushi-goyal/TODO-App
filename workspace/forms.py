from django import forms
from .models import *


class workplaceform(forms.ModelForm):
    class Meta:
        model = Addworkplace
        widgets = {
            "title": forms.TextInput(attrs={'placeholder': "Ex: Shopping List"})
        }
        fields = '__all__'


class taskform(forms.ModelForm):
    class Meta:
        model = Addtask
        widgets = {
            "task": forms.TextInput(attrs={'placeholder': "Add Task"})
        }
        fields = "__all__"
