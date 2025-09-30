from django import forms
from  .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Your name'}),
            'email': forms.EmailInput(attrs={'Placeholder':'you@example.com'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message...'})
        }
