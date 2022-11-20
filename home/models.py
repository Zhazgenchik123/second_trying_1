from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=100)
    full_text_1 = models.TextField('статья-1', null=True, blank=True)
    full_text_2 = models.TextField('статья-2', null=True, blank=True)
    full_text_3 = models.TextField('статья-3', null=True, blank=True)
    full_text_4 = models.TextField('статья-4', null=True, blank=True)
    full_text_5 = models.TextField('статья-5', null=True, blank=True)
    full_text_6 = models.TextField('статья-6', null=True)

    date = models.DateField('Дата публикации')
    image = models.ImageField(upload_to='media/img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'