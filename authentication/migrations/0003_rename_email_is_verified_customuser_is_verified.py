# Generated by Django 4.0.10 on 2023-12-18 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customuser_lastname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='email_is_verified',
            new_name='is_verified',
        ),
    ]