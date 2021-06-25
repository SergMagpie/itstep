from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Words(models.Model):
    word = models.CharField(max_length=255, verbose_name='word')
    translate = models.CharField(max_length=255, verbose_name='translate')
    learned = models.BooleanField(default=False, verbose_name='learned')
    creator = models.ForeignKey(User, blank=False,
                            on_delete=models.CASCADE)