from django.db import models

from django.utils import timezone
import datetime

#models.ForeignKey(name_class, on_delete = models.CASCADE)
class Comment(models.Model):
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField('текст комментария', max_length=200)
    date = models.DateTimeField('дата комментария')

    def __str__(self):
        return self.author_name

    def waz_comment_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


