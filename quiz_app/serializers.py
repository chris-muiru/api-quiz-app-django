from dataclasses import fields
from rest_framework import serializers
from .models import QuizModel, ScoreModel


class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer to serialize fields from QuizModel
    Args:
        ModelSerializer
    """
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = QuizModel
        fields = ['id', 'user', 'question', 'answer',
                  'choices', 'discussion', 'isCounted']
        extra_kwargs = {
            'answer': {'write_only': True},
            'isCounted': {'read_only': True}
        }


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreModel
        fields = ['total']
