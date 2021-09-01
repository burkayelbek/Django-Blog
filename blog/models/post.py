from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from blog.abstract_models import DateAbstractModel # Temelde model sadece içinde barındırıyor

class PostModel(DateAbstractModel): # models.Model' yazısını kaldırdık
    image = models.ImageField(upload_to='post_images')
    title = models.CharField(max_length=50)
    content = RichTextField()
    # created_date = models.DateTimeField(auto_now_add=True) # Yazılar tablosu bir kayıt oluşturulduğu zaman oluşturulma tarihi otomatik olarak belirlenecek. Timezone ile yapılabilir.
    # edited_date = models.DateTimeField(auto_now=True) # İçerik her değiştirildiğinde düzenlenme tarihi otomatik yenilenecek.
    slug = AutoSlugField(populate_from="title",unique=True)
    categories = models.ManyToManyField(CategoryModel,related_name='post') # 1 yazı, 1 den fazla kategoriye atılabilir.
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey('account.CustomuserModel', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        db_table = 'post'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self):
        return self.title