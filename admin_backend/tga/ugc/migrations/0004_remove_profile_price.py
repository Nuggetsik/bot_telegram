# Generated by Django 4.1.2 on 2022-10-30 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0003_alter_profile_options_profile_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='price',
        ),
    ]