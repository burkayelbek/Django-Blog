# Generated by Django 3.2.6 on 2021-09-01 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_contactmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='updated_date',
            new_name='edited_date',
        ),
    ]
