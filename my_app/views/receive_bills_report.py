from my_app.models.receive_bills import ReceiveBills
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def receive_bills_report(request: HttpRequest):
  receive_bills = None
  if request.method == 'POST':
    data = request.POST
    _receive_date = data['receive_date']
    receive_bills = ReceiveBills.objects.all().filter(receive_date__lte=_receive_date)
    return render(request, 'report/receive_bills.html', { 'receive_bills': receive_bills })
  else:
    return render(request, 'report/receive_bills.html', { 'receive_bills': receive_bills })