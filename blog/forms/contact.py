from django import forms
from blog.models import ContactModel

# class ContactForm(forms.Form):
#     email = forms.EmailField(label='E-Mail',max_length=50)
#     name_surname = forms.CharField(label='Name Surname', max_length=25)
#     message = forms.CharField(label='Your Message', widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name_surname','email','message')