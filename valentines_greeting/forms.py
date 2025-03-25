from django import forms
from .models import Card

class Cardform(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['name', 'quote', 'image', 'status','user_id']  # Excluding 'author' (set automatically)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Card Name'}),
            'quote': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your quote'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'user_id':forms.TextInput(attrs={
                'type':"hidden"
            })
        }

        labels = {
            'name': 'To',
            'quote': 'Quote',
            'image': 'Upload Image',
            'status': 'Proposal Accepted',
        }