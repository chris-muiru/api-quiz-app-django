from dataclasses import fields
from rest_framework import serializers
from .models import QuizModel


class QuizSerializer(serializers.ModelSerializer):
    """
    Serializer to serialize fields from QuizModel
    Args:
        ModelSerializer
    """
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = QuizModel
        fields = ['id','user','question', 'answer','choices', 'discussion']
