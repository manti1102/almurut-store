from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


from users.managers import CustomUserManager



# Create your models here.
class CustomUser(AbstractUser):

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True, db_index=True)

    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=25)

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

