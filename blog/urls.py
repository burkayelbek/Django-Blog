from django.contrib import admin
from django.urls import path
from blog.views import contact, homepage, category

urlpatterns = [
    path('',homepage , name='homepage'),
    path('contact',contact, name = 'contact'),
    path('category/<slug:categorySlug>', category , name="category")
]
