from home.modules.finance.models import Shop
from home.Helpers.room import *
from django.shortcuts import render, redirect
from home.modules.finance.view.products.forms import ProductForm
from home.modules.finance.models import RoomProduct
from ..views import *


def product_list(request):
    return common_list(request=request,
                         _class=RoomProduct,
                         template='products/products_list.html')


def add_product(request):
    return common_create(request=request,
                         _class=ProductForm,
                         url='products_list',
                         template='products/add_product.html',
                         link=True)


def edit_product(request, pk):
    return common_edit(request=request,
                       _class=RoomProduct,
                       pk=pk,
                       _form=ProductForm,
                       url='products_list',
                       template='products/edit_product.html',
                       link=True)
    # context = get_context(request)
    # product = RoomProduct.objects.get(pk=pk)
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('products_list')
    #     else:
    #         context['error'] = 'form is invalid'
    # form = ProductForm(instance=product)
    # context['form'] = form
    # return render(request, 'products/edit_product.html', context)