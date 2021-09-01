from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import CustomUserModel



class CustomAdmin(UserAdmin):
    model = CustomUserModel
    list_display=('username','email')
    # Avatar ekleme alanı için yapıldı.
    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Change Area',{
                'fields':['avatar']
            }),
    )
    

admin.site.register(CustomUserModel,CustomAdmin)