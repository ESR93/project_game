from django.shortcuts import render
from .serializers import QuestionsSerializer, ChoicesSerializer, AnswersSerializer, QuestionsAnsweredSerializer
from .models import Questions, Choices, UserAnswers
from rest_framework import generics


# Create your views here.

class QuestionsViewSet(generics.ListCreateAPIView):
    serializer_class = QuestionsSerializer
    queryset = Questions.objects.all()

class AnswersViewSet(generics.ListCreateAPIView):
    serializer_class = AnswersSerializer
    queryset = UserAnswers.objects.all()

class QuestionAnswersViewSet(generics.ListAPIView):
    serializer_class = QuestionsAnsweredSerializer
    queryset = Questions.objects.all()

def index(request):
    return render(request, 'gmat_questions/index.html')

def stats(request):
    return render(request, 'gmat_questions/stats.html')