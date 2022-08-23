from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import UpdateTextFormModel
from django.contrib.auth.decorators import login_required
from blog.models import PostModel


@login_required(login_url='/')
def update_text(request, slug):
    text = get_object_or_404(PostModel, slug=slug, author=request.user)
    form = UpdateTextFormModel(request.POST or None, files=request.FILES or None, instance=text) # Post isteği varsa al veya None dön. Files varsa al veya None dön
    if form.is_valid():
        form.save()
        return redirect('detail', slug=text.slug)
    context = {
        'form':form
    }
    return render(request, 'pages/update-text.html', context=context)