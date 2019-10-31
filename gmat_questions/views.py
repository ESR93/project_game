from django.shortcuts import render
from .serializers import QuestionsSerializer, ChoicesSerializer, AnswersSerializer
from .models import Questions, Choices, UserAnswers
from rest_framework import generics


# Create your views here.

class QuestionsViewSet(generics.ListAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

class AnswersViewSet(generics.ListCreateAPIView):
    serializer_class = AnswersSerializer
    queryset = UserAnswers.objects.all()