from django.db import models
from . import Category

STATUS_CHOICE = (('N','a Receber'), ('S','Recebido'))
class ReceiveBills(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=200, null=True, blank=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='N')
  receive_date = models.DateField()
  categories = models.ManyToManyField(Category)