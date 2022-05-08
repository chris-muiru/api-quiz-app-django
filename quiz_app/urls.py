from django.urls import path
from .views import QuizListView, QuizDetailsView

urlpatterns = [
    path('', QuizListView.as_view(), name="QuizListView"),
    path('<int:pk>/', QuizDetailsView.as_view(), name="QuizListById")
]
