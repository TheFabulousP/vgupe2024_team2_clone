# Generated by Django 4.0.3 on 2024-03-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_book_description_alter_book_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdfFile',
            field=models.FileField(blank=True, null=True, upload_to='data/book/pdf'),
        ),
    ]