from django import forms
from .models import Supercomputer

class SupercomputerForm(forms.ModelForm):
    class Meta:
        model = Supercomputer
        fields = '__all__'