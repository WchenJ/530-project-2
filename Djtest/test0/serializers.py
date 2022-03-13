from rest_framework import serializers
from .models import User,Healthdata,Device,Divrec,Permission


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name", "age", "role", "birth", "sex"]

class HealthdataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healthdata
        fields = ["id", "permission", "tempreture", "blood_pressure", "pulse", "oximeter","weight", "glucometer","time" ]

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ["divice_id", "sku", "serial_number"]

class DivrecSerializer(serializers.ModelSerializer):
    class Meta:
        model = Divrec
        fields = ["id", "deviceid"]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ["role", "permission"]

