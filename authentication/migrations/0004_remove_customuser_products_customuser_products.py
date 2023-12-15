# Generated by Django 4.0.10 on 2023-12-14 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='products',
        ),
        migrations.AddField(
            model_name='customuser',
            name='products',
            field=models.ManyToManyField(blank=True, to='authentication.products'),
        ),
    ]
