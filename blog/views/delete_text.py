from django.contrib.auth.decorators import login_required
from blog.models import PostModel
from django.shortcuts import get_object_or_404, redirect


@login_required(login_url='/')
def delete_text(request, slug):
    get_object_or_404(PostModel, slug=slug, author=request.user).delete()
    return redirect('my_posts')