from django import forms
from .models import Worlds

class NewWorld(forms.ModelForm):
    class Meta:
        model = Worlds
        fields = ['name']
