# Generated by Django 4.1.2 on 2022-10-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0004_remove_profile_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=1, max_length=140, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]