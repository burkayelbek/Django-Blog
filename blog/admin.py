from django.contrib import admin
from blog.models import (
    CategoryModel, PostModel, CommentModel, ContactModel
) 

admin.site.register(CategoryModel)

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title','content') # Django admin üzerinde arama yapmak için oluşturulmuştur.
    list_display = (
        'title', 'created_date', 'edited_date' # Admin panel üzerinde bu alanların gösterilmesini sağlar.
    )

# admin.site.register(PostModel,PostAdmin)

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display=( 'writer', 'created_date','edited_date') # Abstract modelin içinde edited_date olarak oluşturulduğundan dolayı bu alanı değiştirdik.
    search_fields = ('writer__username',)
    # list_display=(
    #     'writer', 'created_date','updated_date'
    # )
    
#admin.site.register(CommentModel, CommentAdmin)

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('email',)
    list_display=(
        'email', 'created_date'
    )
#admin.site.register(ContactModel, ContactAdmin)