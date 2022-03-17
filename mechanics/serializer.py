from rest_framework import serializers
from .models import Client,Mechanic,User

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user','email')

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ('user','email')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_employee','is_customer','username')

