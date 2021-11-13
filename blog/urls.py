from django.contrib import admin
from django.urls import path
from blog.views import contact, homepage, category, my_posts, detail

urlpatterns = [
    path('',homepage , name='homepage'),  #name parametresi base html içinde bulunan html dosyalarında url 'homepage' yönlendirmesi için yapılmaktadır.
    path('contact',contact, name = 'contact'),
    path('category/<slug:categorySlug>', category , name='category'),
    path('my-posts', my_posts, name = 'my_posts'),
    path('detail/<slug:slug>', detail , name='detail'),
]
