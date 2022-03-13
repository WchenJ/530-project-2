from rest_framework import serializers
from .models import User,Healthdata


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "age", "role", "birth", "sex"]

class HealthdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthdata
        fields = ["id", "permission", "tempreture", "blood_pressure", "pulse", "oximeter","weight", "glucometer","time" ]


