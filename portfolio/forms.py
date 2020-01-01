from django import forms

# Contact Form (in the footer)
class ContactForm(forms.Form):
    contactName = forms.CharField(required=True)
    contactEmail = forms.EmailField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea)

    # customization
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contactName'].label = "Votre nom"
        self.fields['contactEmail'].label = "Votre adresse mail"
        self.fields['message'].label ="Votre message.."