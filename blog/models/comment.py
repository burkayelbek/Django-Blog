from django.db import models
from django.contrib.auth.models import User
from blog.models import PostModel
from blog.abstract_models import DateAbstractModel # Temelde model sadece içinde barındırıyor

class CommentModel(DateAbstractModel): # models.Model' yazısını kaldırdık
    #writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post") # Eğer kullanıcı silinirse yorumları silinecek / Yazan kişinin yorumlarına erişilebilir.
    writer = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name="comment") # Eğer kullanıcı silinirse yorumları silinecek / Yazan kişinin yorumlarına erişilebilir.
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name="comments") # Yazı sinilirse o yazıya ait yorumlar silinecek 
    # Related name ile ters ilişiki kuruluyor. Yazının yorumlarına erişebilir
    comment = models.TextField()
    # created_date = models.DateTimeField(auto_now_add=True) # Oluşturma tarihini yaz
    # updated_date = models.DateTimeField(auto_now=True) # Güncellenme tarihini yaz

    class Meta:
        db_table = 'comment'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
    
    def __str__(self):
        return self.writer.username