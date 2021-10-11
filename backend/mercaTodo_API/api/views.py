from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Products
import json


# Create your views here.

class ProductsView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request):
    productsList = list(Products.objects.values())
    if len(productsList) > 0:
      data={'message':'Succes', 'products':productsList}
    else:
      data={'message':'Products not found...'}
    return JsonResponse(data)

  def post(self, request):
    #print(request.body)
    jd=json.loads(request.body)
    #print(jd)
    Products.objects.create(prod_description=jd['prod_description'], prod_unit_price=jd['prod_unit_price'], prod_stock=jd['prod_stock'], cat_id=jd['cat_id'], prov_id=jd['prov_id'], prod_datetime_ingress=jd['prod_datetime_ingress'] )
    data={'message':'Succes'}
    return JsonResponse(data)

  def put(self, request):
    pass

  def delete(self, request):
    pass
