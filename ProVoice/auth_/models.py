from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_rates = models.IntegerField(default=0)
    total_rates = models.IntegerField(default=0)
    
    def set_rate(self, value):
        self.num_rates += 1
        self.total_rates += value
        self.rating = self.total_rates/self.num_rates

class CommentProfile(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')