from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


""" function api """
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     return Response({'name': 'miyankouh'})


""" class base api """
class Home(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)
