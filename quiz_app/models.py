from django.db import models
from django.contrib.auth.models import User


class QuizModel(models.Model):
    user_pk = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.JSONField()
    discussion = models.CharField(max_length=255)

    def __str__(self):
        return self.question
# Create your models here.
