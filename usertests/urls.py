from django.urls import path

from . import views

urlpatterns = [
    path("question/<int:pk>", views.QuestionDetailView.as_view()),
    path("answer/<int:pk>", views.AnswerDetailView.as_view())
]