from django.http.response import HttpResponse
from my_app.models.category import CATEGORY_TYPE_CHOICE
from my_app.models import Category
from django.http.request import HttpRequest
from django.shortcuts import render


def create_category(request: HttpRequest):
  if request.method == 'GET':
    category_type = CATEGORY_TYPE_CHOICE
    return render(request, 'category/create.html', { 'category_type': category_type })
  else:
    data = request.POST
    _name = data['name']
    _description = data['description']
    _type = data['category_type']

    category = Category(name=_name, description=_description, category_type=_type)

    category.save()

    return HttpResponse('Categoria criada com sucesso!')


