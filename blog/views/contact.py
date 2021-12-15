from django.shortcuts import render, redirect
from blog.forms import ContactForm
from blog.models import ContactModel

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = ContactModel()
            contact.email = form.cleaned_data['email']
            contact.name_surname = form.cleaned_data['name_surname']
            contact.message = form.cleaned_data['message']
            contact.save()
            return redirect('homepage')
    context ={
        'form':form
    }
    return render(request, 'pages/contact.html', context=context)
