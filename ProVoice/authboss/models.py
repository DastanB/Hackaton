from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class University(models.Model):
    name = models.CharField(max_length=255)

class User(AbstractUser):
    def get_username(self):
        if self.profile.show_name:
            return self.get_full_name()
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_name = models.BooleanField('Показать имя на сайте', default=False)
    age = models.IntegerField()
    tel = models.CharField(max_length=20)
    teacher = models.BooleanField(default=False)
    student = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.get_username()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
