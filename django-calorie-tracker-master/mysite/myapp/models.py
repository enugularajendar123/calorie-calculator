from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Food(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()


class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)
GENDER_CHOICES=(('M','Male'),('F','Female'))
class register(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    address=models.TextField()
    phonenumber=models.IntegerField()
    gender=models.CharField(choices=GENDER_CHOICES,max_length=128)

