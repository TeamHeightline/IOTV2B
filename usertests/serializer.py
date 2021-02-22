from rest_framework import serializers
from .models import Question, Answer


# class AnswerSerializer(serializers.Serializer):
#     class Meta:
#         model: Answer
#         fields = ['textV1', 'video_url', 'check_queue', 'hard_level_of_answer']
#


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    theme = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    author = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
