from django.db import models


class DateAbstractModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True) # Oluşturma tarihini yaz
    edited_date = models.DateTimeField(auto_now=True) # Güncellenme tarihini yaz

    class Meta:
        abstract = True