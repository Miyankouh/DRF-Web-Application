from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from .models import Person, Question, Answer
from permissions import IsOwnerOrReadOnly

""" function api """
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     return Response({'name': 'miyankouh'})


""" class base api """
class Home(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser,]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class QuestionListView(APIView):
    throttle_scope = 'questions'

    def get(self, request):
        questions = Question.objects.all() 
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    
class QuestionCreateView(APIView):
    """  
        Cerate a new question
    """
    # permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
