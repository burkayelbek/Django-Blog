from django.core import paginator
from django.shortcuts import render, get_object_or_404
from blog.models import PostModel, CategoryModel
from django.core.paginator import Paginator #Sayfalama için kullanıyoruz.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def my_posts(request):
    posts = request.user.posts.order_by('-id') # Post modelinden author related name('posts' buradan gelmektedir.) üzerinden çektik.
    page = request.GET.get('page')
    paginator = Paginator(posts,1) #Which post and how many page sliced

    return render(request,'pages/my-posts.html',context={
        'posts':paginator.get_page(page),
    })