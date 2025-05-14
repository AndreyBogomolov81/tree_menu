from django.db import models
from django.urls import reverse


# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=160)
    url = models.URLField(blank=True, null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return f'MenuItem(id={self.id}, title={self.title})'

    def save(self, *args, **kwargs):
        '''
        Переопределение метода save для формирования url пункта меню
        :param args:
        :param kwargs:
        :return:
        '''
        # для исключения цикличных ссылок
        from .utils import get_url_for_item
        if not self.url:
            self.url = get_url_for_item(self)
        super().save(*args, **kwargs)



