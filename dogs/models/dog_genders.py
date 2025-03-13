from django.db import models


class DogGender(models.Model):
    name = models.CharField(max_length=10, unique=True,)

    class Meta:
        verbose_name = 'Пол собаки'
        verbose_name_plural = 'Пол собак'

    def __str__(self):
        return self.name
