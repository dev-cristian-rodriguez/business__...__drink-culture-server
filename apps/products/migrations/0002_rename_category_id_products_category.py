# Generated by Django 5.2 on 2025-05-10 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]
