# Generated by Django 3.2.6 on 2021-08-18 19:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210818_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]