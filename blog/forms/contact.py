from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(max_length=50)
    name_surname = forms.CharField(max_length=25)
    message = forms.CharField(widget=forms.Textarea)