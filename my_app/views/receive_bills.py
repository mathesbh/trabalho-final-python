from django.http.response import HttpResponse
from my_app.models.receive_bills import ReceiveBills, STATUS_CHOICE
from my_app.models.category import Category
from django.http.request import HttpRequest
from django.shortcuts import redirect, render, resolve_url

def create_receive_bills(request: HttpRequest):
  categories = Category.objects.filter(category_type='R')
  if request.method == 'GET':
    status = STATUS_CHOICE
    return render(request, 'finances/receive/create.html', {
      'status': status,
      'categories': categories,
    })
  else:
    data = request.POST
    _value = data['value']
    _description = data['description']
    _receive_date = data['receive_date']
    _status = data['status']
    _category_id = data['category']

    category = Category.objects.get(id=_category_id)

    receive_bills = ReceiveBills(value=_value, description=_description, receive_date=_receive_date, status=_status)

    receive_bills.save()

    receive_bills.categories.add(category)

    return redirect(resolve_url('home'))
