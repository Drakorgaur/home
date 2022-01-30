from django.db import models
from welcome.models import User

class DebtWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Debt(models.Model):
    wallet = models.ForeignKey(DebtWallet, on_delete=models.CASCADE, related_name='wallet')
    debtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debtor')
    amount = models.FloatField()
    repay = models.FloatField(default=0)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "[ {} ] to [ {} ] | {}".format(str(self.debtor), str(self.wallet), str(self.amount))

class Repay(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='debt')
    amount = models.FloatField()
    description = models.CharField(max_length=200, blank=True)