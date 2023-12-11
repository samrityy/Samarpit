# Generated by Django 4.0.10 on 2023-12-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_products_customuser_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='email_is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
