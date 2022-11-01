from distutils.command.upload import upload
from django.db import models
from .validators import validate_file_size



# Create your models here.
class Profile(models.Model):
    name = models.TextField(
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание', max_length=140
    )
    get_image = models.ImageField(
        verbose_name='Изображение',upload_to='pictures/%Y/%m/%d/',
        validators=[validate_file_size] 
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена'
    )

    def __str__(self):
        return f'#{self.name}'

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
