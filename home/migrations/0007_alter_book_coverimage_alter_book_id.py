# Generated by Django 4.2.11 on 2024-03-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_book_pdffile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='coverImage',
            field=models.ImageField(blank=True, null=True, upload_to='home/static/data/book/coverImage'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
