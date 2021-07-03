from django.db import models
from django.db.models.aggregates import Sum
from . import Category

STATUS_CHOICE = (('N','a Receber'), ('S','Recebido'))

class ReceiveBillsManager(models.Manager):
  def get_sum_receive_month(self, month, year):
    sum_month = float(ReceiveBills.objects.filter(receive_date__month=month, receive_date__year=year).aggregate(Sum('value'))['value__sum'] or 0)
    return sum_month
  
  def get_sum_receives_category(self, month, year):
    categories = Category.objects.all().count()
    receives = []

    for i in range(1, categories):
      sum_receives = float(ReceiveBills.objects.filter(receive_date__month=month, receive_date__year=year, category=i).aggregate(Sum('value'))['value__sum'] or 0)
      pay = {
        'category': Category.objects.get(id=i),
        'sum_receives': sum_receives
      }
      if sum_receives > 0:
        receives.append(pay)
      
    return receives

class ReceiveBills(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=200, null=True, blank=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='N')
  receive_date = models.DateField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  objects = ReceiveBillsManager()