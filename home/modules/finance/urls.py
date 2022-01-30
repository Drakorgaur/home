from django.urls import path
from .views import *

urlpatterns = [
    path('finance/', finance_index, name='finance'),
    path('finance/debts/', debts, name='debts'),
    path('finance/debts/add', add_debt, name='add_debt'),
]

urlpatterns += [
    path('finance/debts/repay/add', add_repay, name='add_repay'),
]