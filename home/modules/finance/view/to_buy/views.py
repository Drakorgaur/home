from ...models import ToBuy
from .forms import ToBuyForm
from ..views import *

def add_tobuy(request):
    context = get_context(request)
    if request.method == 'POST':
        form = ToBuyForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.creator = request.user
            obj.active = True
            obj.save()
            return redirect(tobuy_list)
        else:
            context['error'] = 'form is invalid'
    form = ToBuyForm()
    context['form'] = form
    return render(request, 'tobuy/add_tobuy.html', context)


def edit_tobuy(request, pk):
    return common_edit(request=request,
                       _class=ToBuy,
                       pk=pk,
                       _form=ToBuyForm,
                       url='tobuy_list',
                       template='tobuy/edit_tobuy.html',
                       link=True)


def tobuy_list(request):
    return common_list(request=request,
                         _class=ToBuy,
                         template='tobuy/tobuy_list.html')


def delete_tobuy(request, pk):
    return common_delete(request=request,
                         _class=ToBuy,
                         pk=pk,
                         redirect_to='tobuy_list')