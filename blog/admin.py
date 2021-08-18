from django.contrib import admin
from blog.models import CategoryModel, PostModel

admin.site.register(CategoryModel)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','content') # Django admin üzerinde arama yapmak için oluşturulmuştur.
    list_display = (
        'title', 'created_date', 'edited_date' # Admin panel üzerinde bu alanların gösterilmesini sağlar.
    )

admin.site.register(PostModel,PostAdmin)

