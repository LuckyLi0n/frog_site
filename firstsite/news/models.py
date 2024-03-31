from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', default='Без названия', max_length=100)
    anons = models.CharField('Анонс', default=' ', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'




