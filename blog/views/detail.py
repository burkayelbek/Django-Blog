from django.shortcuts import get_object_or_404, render
from blog.models import PostModel

def detail(request, slug):
    post = get_object_or_404(PostModel, slug = slug)
    comments = post.comments.all()
    return render(request, 'pages/detail.html', context={
        'post': post,
        'comments':comments # 'comments' olarak yaptığımız alan html tarafına gönderdiğimiz yerdir. Diğeri ise veriyi logic olarak alıp adlandırdığımız alandır.
    })