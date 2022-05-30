from django.urls import path
from .views import QuizListView, QuizDetailsView,ScoreView
urlpatterns = [
    path('', QuizListView.as_view(), name="QuizListView"),
    path('<int:pk>/', QuizDetailsView.as_view(), name="QuizListById"),
    path('score/',ScoreView.as_view(), name="Score")
]
