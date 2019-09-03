from django.db import models

#models.ForeignKey(name_class, on_delete = models.CASCADE)
class Comment(models.Model):
    author_name = models.CharField('имя автора', max_length = 50)
    comment_text = models.CharField('текст комментария', max_length = 200)
    date = models.DateTimeField('дата комментария')

