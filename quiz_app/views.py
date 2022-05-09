from rest_framework.views import APIView
from rest_framework import status, request
from rest_framework.response import Response
from .serializers import QuizSerializer
from .models import QuizModel


class QuizListView(APIView):
    def get(self, request):
        query = QuizModel.objects.all()
        serializer = QuizSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            if not QuizModel.objects.filter(question=serializer.validated_data['question']).exists():
                serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# crud functionality


class QuizDetailsView(APIView):
    def get(self, request, pk):
        query = QuizModel.objects.get(id=pk)
        serializer = QuizSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        query = QuizModel.objects.get(id=pk)
        serializer = QuizSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        quiz = QuizModel.objects.get(id=pk).delete()
        return Response(status=status.HTTP_200_OK)
# Create your views here.
