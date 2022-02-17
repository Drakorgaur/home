from django.db import models
from welcome.models import User
from home.models import Room
from django.db.models import JSONField

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
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='debt_creator')

    def __str__(self):
        if self.description:
            return "[ debtor: {} ]  {} - {}".format(str(self.debtor), str(self.description), str(self.amount))
        return "[ {} ] to [ {} ] | {}".format(str(self.debtor), str(self.wallet), str(self.amount))

    def field_names(self):
        return ['wallet', 'debtor', 'amount', 'repay', 'description', 'creator']


class Repay(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='debt')
    amount = models.FloatField()
    description = models.CharField(max_length=200, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='repay_creator')


class Shop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    Choices = (
        ('fr', 'fruits'),
        ('mk', 'milk'),
        ('hg', 'hygiene'),
        ('sw', 'sweat'),
        ('br', 'bread'),
        ('ch', 'chemical'),
        ('ot', 'other'),
    )
    name = models.CharField(max_length=200)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='shop', blank=True,
                             null=True)
    cost = models.FloatField()
    per_kg = models.BooleanField()
    category = models.CharField(max_length=50, choices=Choices)

    class Meta:
        abstract=True


class GeneralProducts(Product):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='gen_shop')
    updated = models.DateField()

    def __str__(self):
        return "{} [{}]".format(str(self.name), str(self.shop))


class RoomProduct(Product):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rp_room')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='rp_shop')
    synchronized = models.DateField(null=True)

    def __str__(self):
        return self.name


class Buy(models.Model):
    cost = models.FloatField()
    weight = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class ToBuy(Buy):
    product = models.ForeignKey(RoomProduct, on_delete=models.RESTRICT, related_name='tb_product')
    shop = models.ForeignKey(Shop, on_delete=models.RESTRICT, related_name='tb_shop', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tb_creator')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='tobuy_room',
                             null=True)
    active = models.BooleanField(blank=False)


    def __str__(self):
        return str(self.product)


class Bought(models.Model):
    date = models.DateField(default='2001-01-01')
    receipt = JSONField()
    cost = models.FloatField()
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bgh_creator')
    shop = models.ForeignKey(Shop, on_delete=models.RESTRICT, related_name='bgh_shop', blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bought_room',
                             null=True)


    def __str__(self):
        return "[{}] {}".format(str(self.date), str(self.buyer))