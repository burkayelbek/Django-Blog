from audioop import add
from django.contrib import admin
from django.urls import path
from blog.views import contact, homepage, category, my_posts, detail, add_text, update_text, delete_text

urlpatterns = [
    path('',homepage , name='homepage'),  #name parametresi base html içinde bulunan html dosyalarında url 'homepage' yönlendirmesi için yapılmaktadır.
    path('contact',contact, name = 'contact'),
    path('category/<slug:categorySlug>', category , name='category'),
    path('my-posts', my_posts, name = 'my_posts'),
    path('detail/<slug:slug>', detail , name='detail'),
    path('add-text', add_text, name='add-text'),
    path('update-text/<slug:slug>', update_text, name='update-text'),
    path('delete-text/<slug:slug>', delete_text, name='delete-text'),
]
