from django.db import models
from autoslug import AutoSlugField

class CategoryModel(models.Model):
    name = models.CharField(max_length=30,blank=False,null=False)
    # Dinamik url oluşturmak için kullanılır. Ex: burkayelbek/test OR burkayelbek/test2 
    # Unique olması sayesinde her kategori isimleri aynı olabilir ama slug alanları farklı olacaktır.
    slug = AutoSlugField(populate_from="name",unique = True) 

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories' # Blog app altında "Category model" olarak gözüken yazıyı "Categories" olarak değiştirir.
        verbose_name = 'Category' # Select "Category" yazan kısımdır.

    def __str__(self):
        return self.name # Categories modeline django-admin üzerinde bakıldığı zaman içinde bulunan objeleri "object" yerine isimleriyle gösterir.
    



