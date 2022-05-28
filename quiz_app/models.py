from django.db import models
from django.contrib.auth.models import User


class QuizModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    choices = models.JSONField()
    discussion = models.CharField(max_length=255)
    isCounted = models.BooleanField(default=False)
    def __str__(self):
        return self.question


class ScoreModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.user} {self.total}'
# Create your models here.
