# Generated by Django 4.2.11 on 2024-04-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_user_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.IntegerField(choices=[(0, 'article'), (1, 'book'), (2, 'magazine'), (3, 'video/audio'), (4, 'comic'), (5, 'other')], default=0),
        ),
    ]