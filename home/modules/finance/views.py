from django.shortcuts import render
from .models import Debt, DebtWallet, Repay
from .forms import DebtForm, RepayForm
from django.shortcuts import redirect

#Helpers
def get_context(request):
    """
    Returns context that contains User, his Debts and Repays for his Debts
    """
    context = dict()
    context['user'] = request.user
    try:
        context['debts'] = Debt.objects.filter(wallet=get_wallet(request))
    except Debt.DoesNotExist:
        context['debts'] = None

    repays = list()
    for debt in context['debts']:
        try:
            repays += Repay.objects.filter(debt=debt)
        except Debt.DoesNotExist:
            repays = None
            break
    context['repays'] = repays
    return context



def get_wallet(request):
    try:
        return DebtWallet.objects.get(user=request.user)
    except DebtWallet.DoesNotExist:
        return None

#debts
def debts(request):
    context = get_context(request)
    return render(request, 'debts.html', context)

def add_debt(request):
    context = get_context(request)
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            debt = form.save(commit = False)
            wallet = get_wallet(request)
            if wallet is not None:
                debt.wallet = wallet
            else:
                context['error'] = 'You are trying to add debt to account that have no Wallet. ' \
                                   'Please create wallet before continue'
                return render(request, 'debts.html', context)
            debt.creator = request.user
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
def add_repay(request, debt_id=None):
    context = get_context(request)
    if request.method == 'POST':
        form = RepayForm(request.POST)
        if form.is_valid():
            repay = form.save(commit=False)
            repay.creator = request.user
            repay.save()
            return redirect('debts')
        else:
            form = RepayForm()
            context['form'] = form
            context['error'] = 'form is invalid'
            return render(request, 'repays/add_repay.html', context)
    else:
        if debt_id:
            try:
                context['debts'] = Debt.objects.filter(wallet=get_wallet(request))
            except Debt.DoesNotExist:
                context['debts'] = None
        form = RepayForm(initial={'debt': context['debts']})
        context['form'] = form
        return render(request, 'repays/add_repay.html', context)

def repay_approve(request, repay_id=None):
    context = get_context(request)
    repay = Repay.objects.get(pk=repay_id)
    if request.user != repay.creator:
        repay.debt.amount -= repay.amount
        repay.debt.save()
        repay.delete()
        return redirect('debts')
    context['error'] = 'Creator of Repay can not approve it. ' \
                       'Wait until 2nd person will approve it.'
    return render(request, 'debts.html', context)
    # TODO: create answer that user have no rights to do it

def repay_decline(request, repay_id=None):
    repay = Repay.objects.get(pk=repay_id)
    repay.delete()
    return redirect('debts')

#Finance
def finance_index(request):
    return render(request, 'finance.html', {'user': request.user})

