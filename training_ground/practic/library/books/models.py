from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    year_of_publication = models.PositiveSmallIntegerField()
    author = models.ForeignKey('Author',
                               on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    surname = models.CharField(max_length=255, verbose_name='surname')
    year_of_birth = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
