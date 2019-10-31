from rest_framework import serializers
from .models import Questions, Choices, UserAnswers

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['id', 'choices_text', 'correct']


class QuestionsSerializer(serializers.ModelSerializer):
    answers = ChoicesSerializer(read_only=True, many=True, source = 'question_answer')
    class Meta:
        model = Questions
        fields = ['id', 'question_type','question_context','image','question_text','answers']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ['id','choice_id','question_number','time_spent','correct']

