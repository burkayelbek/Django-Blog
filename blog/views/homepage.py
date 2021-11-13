from django.core import paginator
from django.shortcuts import render
from blog.models import PostModel
from django.core.paginator import Paginator #Sayfalama için kullanıyoruz.
from django.db.models import Q

def homepage(request):
    query = request.GET.get('query') #url içinde ?query=deneme gibi aramak için kullandık.
    posts = PostModel.objects.order_by('-id')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    page = request.GET.get('page') # url tarafında ?page=2 gibi sorgu yapmamızı sağlar.
    paginator = Paginator(posts,2) #Which post and how many page sliced

    return render(request,'pages/homepage.html',context={
        'posts':paginator.get_page(page)
    })