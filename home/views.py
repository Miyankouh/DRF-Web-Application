from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer

""" function api """
# @api_view(['GET', 'POST', 'PUT'])
# def home(request):
#     return Response({'name': 'miyankouh'})


""" class base api """
class Home(APIView):
    def get(self, request):
        persons = Person.objects.get(name='miyankouh')
        ser_data = PersonSerializer(instance=persons)
        return Response(data=ser_data.data)
