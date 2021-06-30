from my_app.models import category
from my_app.models.category import Category
from my_app.models import PayBills, ReceiveBills
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def cash_flow(request: HttpRequest):
  if request.method == 'GET':
    return render(request, 'finances/cash_flow/create.html')
  else:
    data = request.POST
    initial_balance = data['initial_balance']
    start_date = data['start_date']
    end_date = data['end_date']
    pay_bills_due_date = PayBills.objects.filter(due_date__range=(start_date, end_date))
    receive_bills_date = ReceiveBills.objects.filter(receive_date__range=(start_date, end_date))

    total_pay_bills = 0
    total_receive_bills = 0

    total = 0

    for pay_bills in pay_bills_due_date:
      total_pay_bills += pay_bills.value

    for receive_bills in receive_bills_date:
      total_receive_bills += receive_bills.value

    total = (total_receive_bills - total_pay_bills) + float(initial_balance)
   

    return render(request, 'finances/cash_flow/report.html', {
      'initial_balance': initial_balance,
      'start_date': start_date,
      'end_date': end_date,
      'pay_bills': pay_bills_due_date,
      'receive_bills': receive_bills_date,
      'total_pay_bills': total_pay_bills,
      'total_receive_bills': total_receive_bills,
      'total': total,      
    })

    