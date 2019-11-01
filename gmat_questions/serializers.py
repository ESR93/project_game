from rest_framework import serializers
from .models import Questions, Choices, UserAnswers

class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choices
        fields = ['id', 'choices_text', 'correct']


class QuestionsSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(read_only=True, many=True, source = 'question_answer')
    class Meta:
        model = Questions
        fields = ['id', 'question_type','question_context','image','question_text','choices']


class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ['id','choice_id','question_number','time_spent','correct']

class QuestionsAnsweredSerializer(serializers.ModelSerializer):
    answers = AnswersSerializer(read_only=True, many=True, source = 'answer_choice')
    class Meta:
        model = Questions
        fields = ['id', 'question_type','answers']

