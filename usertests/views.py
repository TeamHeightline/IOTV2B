from django.shortcuts import render

# Create your views here.
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView


class QuestionDetailView(APIView):

    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)


class AnswerDetailView(APIView):
    def get(self, request, pk):
        answer = Answer.objects.get(id=pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)