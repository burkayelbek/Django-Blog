from django.contrib import admin
from django.urls import path
from blog.views import contact, homepage

urlpatterns = [
    path('',homepage),
    path('contact',contact)
]
