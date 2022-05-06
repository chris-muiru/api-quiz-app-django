from django.db import models


class Quiz(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_lenght=255)
    answer = models.CharField(max_lenght=255)
    choices = models.JSONField()
    discussion = models.TextField(),
# Create your models here.
