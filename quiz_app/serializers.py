from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import QuizModel


class QuizSerializer(ModelSerializer):
    """
    Serializer to serialize fields from QuizModel
    Args:
        ModelSerializer
    """
    class Meta:
        # todo: remove user_pk
        model = QuizModel
        fields = ['user_pk', 'question', 'answer', 'discussion']
