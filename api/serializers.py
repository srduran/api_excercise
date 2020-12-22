from rest_framework import serializers
from .models import Monkey

class MonkeySerializers(serializers.ModelSerializer):
  """serializer the monkey model to send data to api"""
  class Meta:
    model = Monkey
    fields = ('id', 'name', 'fleas')