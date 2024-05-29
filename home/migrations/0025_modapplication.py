# Generated by Django 4.2.11 on 2024-04-18 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_book_manual'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicantDocument', models.FileField(blank=True, null=True, upload_to=home.models.getApplicantDocURL)),
                ('applicantText', models.TextField(blank=True, max_length=1500, null=True)),
                ('adminComment', models.TextField(blank=True, max_length=1500, null=True)),
                ('status', models.IntegerField(choices=[(0, 'applying'), (1, 'approved'), (2, 'denied')], default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]