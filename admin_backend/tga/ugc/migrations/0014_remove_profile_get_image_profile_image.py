# Generated by Django 4.1.2 on 2022-10-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0013_rename_img_profile_get_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='get_image',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
