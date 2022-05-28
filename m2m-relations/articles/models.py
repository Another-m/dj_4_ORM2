from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Relationship(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='scopes', verbose_name='Выбрать статью')
    tag = models.ForeignKey('Tags', on_delete=models.PROTECT, related_name='scopes', verbose_name='Выбрать раздел')
    main = models.BooleanField(verbose_name="Основной")

    class Meta:
        verbose_name = 'Подкрепить к разделу'
        verbose_name_plural = 'Подкрепить к разделу'


class Tags(models.Model):
    articles = models.ManyToManyField(Article, through='Relationship', related_name='tags')
    tag = models.CharField(max_length=256, verbose_name='Название раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.tag
