from django.contrib import admin
from blog.models import (
    CategoryModel, PostModel, CommentModel
) 

admin.site.register(CategoryModel)

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','content') # Django admin üzerinde arama yapmak için oluşturulmuştur.
    list_display = (
        'title', 'created_date', 'edited_date' # Admin panel üzerinde bu alanların gösterilmesini sağlar.
    )

admin.site.register(PostModel,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('writer__username',)
    list_display=(
        'writer', 'created_date','updated_date'
    )
admin.site.register(CommentModel, CommentAdmin)