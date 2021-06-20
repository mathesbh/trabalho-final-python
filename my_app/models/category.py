from django.db import models

CATEGORY_TYPE_CHOICE = (('D','Despesa'), ('R','Receita'))
class Category(models.Model):
  name = models.CharField(max_length=150)
  description = models.CharField(max_length=200, null=True, blank=True)
  category_type = models.CharField(max_length=10, choices=CATEGORY_TYPE_CHOICE, default='D')
  