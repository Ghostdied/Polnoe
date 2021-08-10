from django.db import models
from django.forms import ModelForm



class Callback(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=120, unique=False, verbose_name="Имя")
    phone = models.CharField(null=False, verbose_name="Tелефон",max_length=100)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Дата заявки")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id", "-timestamp"]
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'

class News(models.Model):
    id = models.AutoField
    text = models.TextField(
        ('Text'),
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        ('Created_at'),
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:

        verbose_name = 'Новости'


class Events(models.Model):
    id = models.AutoField
    text = models.TextField(
        ('Text'),
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        ('Created_at'),
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:

        verbose_name = 'События'


