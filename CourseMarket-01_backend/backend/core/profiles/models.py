
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField('Имя', max_length=50)
    mobile = models.CharField("Номер телефона", max_length=20, blank=True)
    mail = models.EmailField('Почта')
    password = models.CharField('Пароль', max_length=50)
   

    def str(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'