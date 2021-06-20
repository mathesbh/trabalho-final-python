from django.db import models
from . import Category

STATUS_CHOICE = (('N', 'a Pagar'), ('S','Pago'))
PAYMENT_CHOICE = (('D','Dinheiro'), ('CD','Débito'), ('CC','Crédito'), ('B','Boleto'))

class PayBills(models.Model):
  value = models.FloatField()
  description = models.CharField(max_length=250, null=True, blank=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='N')
  payment = models.CharField(max_length=10, choices=PAYMENT_CHOICE, default='D')
  due_date = models.DateField(null=True, blank=True)
  pay_date = models.DateField(null=True, blank=True)
  categories = models.ManyToManyField(Category)