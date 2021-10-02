from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static #otomatik olarak media dosyalarını yayınlamak için hazırlanmış fonksiyondur.
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('contact',contact)
    #path('blog/',include('blog.urls')) # www.burkayelbek.com/blog/ path şeklinde arancaktır.
    path('', include('blog.urls')), # anasayfa olacaktır ve include blog.urls'e giderek otomatik dosyalama yapmaktadır. 


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 1.parametre = media_url yorumlaması gerekmektedir. 2.parametre = root yolunu veriyoruz.
