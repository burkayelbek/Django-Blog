from django.core import paginator
from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator #Sayfalama için kullanıyoruz.

def homepage(request):
    posts = PostModel.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(posts,2) #Which post and how many page sliced

    return render(request,'pages/homepage.html',context={
        'posts':paginator.get_page(page)
    })