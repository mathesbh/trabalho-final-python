from django.http.response import HttpResponse
from my_app.models.category import Category
from my_app.models.pay_bills import PAYMENT_CHOICE, PayBills, STATUS_CHOICE
from django.http.request import HttpRequest
from django.shortcuts import render

def create_pay_bills(request: HttpRequest):
  categories = Category.objects.filter(category_type='D')
  if request.method == 'GET':
    payment = PAYMENT_CHOICE
    status = STATUS_CHOICE
    return render(request, 'finances/pay/create.html', {
      'payment': payment,
      'status': status,
      'categories': categories,
     })
  else:
    data = request.POST
    _value = data['value']
    _description = data['description']
    _due_date = data['due_date']
    _pay_date = data['pay_date']
    _payment = data['payment']
    _status = data['status']
    _category_id = data['category']

    category = Category.objects.get(id=_category_id)

    pay_bills = PayBills(value=_value, description=_description, due_date=_due_date, pay_date=_pay_date, payment=_payment, status=_status)

    pay_bills.save()

    pay_bills.categories.add(category)

    pay_bills.save()

    return HttpResponse('Conta a pagar cadastrada com sucesso!')