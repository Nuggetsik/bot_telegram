# Generated by Django 4.1.2 on 2022-10-30 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0007_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='pizza_img',
        ),
    ]
