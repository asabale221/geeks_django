from django.shortcuts import render
from apps.products.models import Products
from apps.settings.models import Setting
# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Products.objects.get(id = id)
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'index.html', context)