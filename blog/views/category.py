from django.core import paginator
from django.shortcuts import render, get_object_or_404
from blog.models import PostModel, CategoryModel
from django.core.paginator import Paginator #Sayfalama için kullanıyoruz.

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel,slug=categorySlug)
    #posts = PostModel.objects.order_by('-id')
    posts = category.post.order_by('-id') # Post modelinden categories related name('post' buradan gelmektedir.) üzerinden çektik.
    page = request.GET.get('page')
    paginator = Paginator(posts,2) #Which post and how many page sliced

    return render(request,'pages/category.html',context={
        'posts':paginator.get_page(page),
        'category_name':category.name
    })