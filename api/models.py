from django.db import models


class Monkey(models.Model):
  """This class is responsable to create a lot of monkeys"""
  name = models.CharField(max_length=36)
  fleas = models.IntegerField(blank=True, null=True)

  def __str__(self):
    """string of this monkey class model"""
    return self.name
