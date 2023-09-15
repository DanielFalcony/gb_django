from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging

from hw2_app.models import Client, Goods, Order

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('Hello page')


def clients_get(request):
    logger.info('Customers list has been requested.')
    result = '<br>'.join(str(i) for i in Client.objects.all())
    return HttpResponse(result)


def goods_get(request):
    logger.info('Goods list has been requested.')
    result = '<br>'.join(str(i) for i in Goods.objects.all())
    return HttpResponse(result)


def orders_get(request):
    logger.info('Order list has been requested.')
    result = '<br>'.join(str(i) for i in Order.objects.all())
    return HttpResponse(result)


def get_orders_by_period(request, client_id, time_for_check):
    client = get_object_or_404(Client, pk=client_id)
    time_ago = datetime.now() - timedelta(days=time_for_check)
    orders = Order.objects.filter(client=client, order_date__gte=time_ago).order_by('-order_date')
    if orders.exists():
        products = Goods.objects.filter(order__in=orders).distinct()
        return render(request, 'hw2_app/get_orders_by_period.html',
                      {'client': client, 'result': products, 'time': time_for_check})
    else:
        return render(request, 'hw2_app/get_orders_by_period.html',
                      {'client': client, 'result': 'Нет заказов!', 'time': time_for_check})
