from django.db import models
from django.contrib.auth.models import User


class QuizModel(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    choices = models.JSONField()
    discussion = models.TextField(),

    def __str__(self):
        return self.question

# Create your models here.
