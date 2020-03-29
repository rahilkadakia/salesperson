from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Manager
        fields = ['user_ref', 'Name', 'Photo', 'Age', 'owner']


class SalespersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Salesperson
        fields = '__all__'


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class TotalTargetsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TotalTargets
        fields = '__all__'


class InventorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'
