from rest_framework import serializers
from ...models import ToBuy, RoomProduct
from welcome.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomProduct
        fields = ['name', 'cost']


class ToBuySerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    creator = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    class Meta:
        model = ToBuy
        fields = ['id', 'product', 'creator', 'weight', 'cost']


def get_porducts_for_tobuy():
    pass