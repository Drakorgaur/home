from .models_factory import *

register(UserFactory)
register(RoomFactory)

def get_room_with_user(linked=True):
    room = get_room()
    user = get_user()
    if linked:
        init_room(room, user)
    else:
        user.save()
    return room, user


def get_room_with_users(amount_of_users):
    room = get_room()
    room.link = 'random'
    room.save()

    users = list()
    for _ in range(amount_of_users):
        user = get_user()
        init_room(room, user)
        users.append(user)
    return room, users


def get_user():
    user = UserFactory.create()
    user.save()
    return user


def get_room():
    room = RoomFactory.create()
    room.link = 'random'
    room.save()
    return room


def get_wallet(user=None):
    wallet = DebtWalletFactory.create()
    if user is not None:
        wallet.user = user
        return wallet
    user = UserFactory.create()
    user.save()
    wallet.user = user
    wallet.save()
    return wallet


def get_debt(owner=None, debtor=None):
    debt = DebtFactory.create()
    if owner is None:
        owner = UserFactory.create()
        owner.save()
    if debtor is None:
        debtor = UserFactory.create()
        debtor.save()
    wallet = get_wallet(owner)
    wallet.save()
    debt.wallet = wallet
    debt.debtor = debtor
    debt.creator = owner
    debt.save()
    return debt


def get_repay(repay_creator=None, debt_owner=None, debt_debtor=None):
    debt = get_debt(debt_owner, debt_debtor)
    repay = RepayFactory.create()
    repay.debt = debt
    repay.amount = repay.debt.amount / 10
    if repay_creator is None:
        creator = get_user()
        creator.save()
        repay.creator = creator
        repay.save()
        return repay
    repay.creator = repay_creator
    repay.save()
    return repay


def get_shop():
    shop = ShopFactory.create()
    shop.save()
    return shop