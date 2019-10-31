from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200, default='')
    question_type = models.CharField(max_length=200, default='')
    question_context = models.CharField(max_length=5000, default='')
    image = models.ImageField(upload_to='images/', blank=True)
    def __str__(self):
        return self.question_text

class Choices(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE,related_name='question_answer')
    choices_text = models.CharField(max_length=200, default='')
    correct = models.BooleanField( blank=True, null=True)
    def __str__(self):
        return self.choices_text

class UserAnswers(models.Model):
    choice_id = models.ForeignKey(Questions, on_delete=models.CASCADE,related_name='answer_choice', blank=True, null=True)
    question_number = models.IntegerField( blank=True, null=True)
    correct = models.BooleanField(blank=True, null=True)
    time_spent = models.FloatField(blank=True, null=True)

