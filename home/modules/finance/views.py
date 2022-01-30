from django.shortcuts import render
from .models import Debt, DebtWallet, Repay
from .forms import DebtForm, RepayForm
from django.shortcuts import redirect

#Helpers
def init_context(request):
    context = dict()
    context['user'] = request.user
    return context

def get_wallet(request):
    return DebtWallet.objects.get(user=request.user)

#debts
def debts(request):
    context = init_context(request)
    debts = Debt.objects.filter(wallet=get_wallet(request))
    repays = list()
    for debt in debts:
        repays += Repay.objects.filter(debt=debt)
    context['debts'] = debts
    context['repays'] = repays
    return render(request, 'debts.html', context)

def add_debt(request):
    context = init_context(request)
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit = False)
            debt.wallet = get_wallet(request)
            debt.save()
            return redirect('debts')
        else:
            context['error'] = 'form is invalid'
            return render(request, 'add_debt.html', context)
    else:
        form = DebtForm()
        context['form'] = form
        return render(request, 'add_debt.html', context)

#debts-repays
def add_repay(request):
    context = init_context(request)
    if request.method == 'POST':
        form = RepayForm(request.POST)
        if form.is_valid():
            repay = form.save()
            return redirect('debts')
        else:
            form = RepayForm()
            context['form'] = form
            context['error'] = 'form is invalid'
            return render(request, 'repays/add_repay.html', context)
    else:
        form = RepayForm()
        context['form'] = form
        return render(request, 'repays/add_repay.html', context)

#Finance
def finance_index(request):
    return render(request, 'finance.html', {'user': request.user})