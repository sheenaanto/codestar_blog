from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    contains the form for collaboration requests
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
