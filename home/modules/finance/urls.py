from django.urls import path
from .views import *

urlpatterns = [
    path('', finance_index, name='finance'),
    path('debts/', debts, name='debts'),
    path('debts/add', add_debt, name='add_debt'),
]

urlpatterns += [
    path('debts/repay/add', add_repay, name='add_repay'),
    path('debts/repay/add/<int:debt_id>', add_repay, name='add_repay'),
    path('debts/repay/approve/<int:repay_id>', repay_approve, name='approve_repay'),
    path('debts/repay/decline/<int:repay_id>', repay_decline, name='decline_repay'),
]