from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)