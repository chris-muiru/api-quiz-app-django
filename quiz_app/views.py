from rest_framework.views import APIView
from rest_framework import status,request
from rest_framework.response import Response

class QuizListView(APIView):
    def get(self,request):
        return Response(status=status.HTTP_200_OK)



# Create your views here.
