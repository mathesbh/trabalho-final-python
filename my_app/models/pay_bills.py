from my_app.models import category
from django.db import models
from django.db.models.aggregates import Sum
from . import Category

STATUS_CHOICE = (('N', 'a Pagar'), ('S','Pago'))
PAYMENT_CHOICE = (('D','Dinheiro'), ('CD','Débito'), ('CC','Crédito'), ('B','Boleto'))

class PayBillsManager(models.Manager):
  def get_sum_pay_month(self, month, year):
    sum_month = float(PayBills.objects.filter(due_date__month=month, due_date__year=year).aggregate(Sum('value'))['value__sum'] or 0)
    return sum_month

  def get_sum_pays_category(self, month, year):
    categories = Category.objects.all().count()
    pays = []

    for i in range(1, categories):
      sum_pays = float(PayBills.objects.filter(due_date__month=month, due_date__year=year, category=i).aggregate(Sum('value'))['value__sum'] or 0)
      pay = {
        'category': Category.objects.get(id=i),
        'sum_pays': sum_pays
      }
      if sum_pays > 0:
        pays.append(pay)
      
    return pays
       

class PayBills(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=250, null=True, blank=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='N')
  payment = models.CharField(max_length=10, choices=PAYMENT_CHOICE, default='D')
  due_date = models.DateField(null=True, blank=True)
  pay_date = models.DateField(null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  objects = PayBillsManager()