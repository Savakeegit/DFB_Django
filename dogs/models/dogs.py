from django.contrib.auth import get_user_model
from django.db import models
from dogs.models.dog_genders import DogGender

User = get_user_model()

class Dog(models.Model):
    name = models.CharField('Кличка', max_length=32)
    gender = models.ForeignKey(DogGender, verbose_name='Пол', on_delete=models.CASCADE)
    breed = models.CharField('Порода', max_length=48)
    color = models.CharField('Окрас', max_length=32)
    date_of_birth = models.DateField('Дата рождения', )
    photo = models.ImageField('Фото', upload_to='dog_photos/%Y/%m/%d/', null=True, blank=True, default='dog_photos/default_dog.jpg',)
    owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)
    extra = models.CharField(max_length=128, null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
