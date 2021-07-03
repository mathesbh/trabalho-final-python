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
    start_date = data['start_date'].split('-')
    end_date = data['end_date'].split('-')
    start_month = int(start_date[1])
    end_month = int(end_date[1])
    year = int(start_date[0])
    result = []
    
    while start_month <= end_month:
      month = {
        'month': start_month,
        'pay_bills':{
          'sum_month': PayBills.objects.get_sum_pay_month(month=start_month, year=year),
          'sum_categories': PayBills.objects.get_sum_pays_category(month=start_month, year=year),
        },
        'receive_bills':{
          'sum_month': ReceiveBills.objects.get_sum_receive_month(month=start_month, year=year),
          'sum_categories': ReceiveBills.objects.get_sum_receives_category(month=start_month, year=year),
        },
        'saldo': float(initial_balance) - PayBills.objects.get_sum_pay_month(month=start_month, year=year) + ReceiveBills.objects.get_sum_receive_month(month=start_month, year=year)
      }
      start_month += 1
      result.append(month)   

    return render(request, 'finances/cash_flow/report.html', {
      'initial_balance': initial_balance,
      'result': result,    
    })

    