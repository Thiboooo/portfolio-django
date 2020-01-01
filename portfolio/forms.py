from django import forms

# Contact Form (in the footer)
class ContactForm(forms.Form):
    contactName = forms.CharField(required=True)
    contactEmail = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)