# File: portfolio/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # This ensures the phone field is displayed correctly (optional, but good practice)
    phone = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        
        # VITAL: All fields must have the 'form-control' class applied here
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'John', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@domain.com', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+254700000000', 'class': 'form-control'}), 
            'message': forms.Textarea(attrs={'placeholder': 'Write your message...', 'rows': 4, 'class': 'form-control'}),
        }