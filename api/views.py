from rest_framework import viewsets
from .models import Monkey
from .serializers import MonkeySerializers

class MonkeyViewSet(viewsets.ModelViewSet):
  """view to show the data from monkey model to the api"""
  queryset = Monkey.objects.all()
  serializer_class = MonkeySerializers
