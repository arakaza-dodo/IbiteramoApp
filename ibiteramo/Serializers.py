from rest_framework import serializers
from .models import *

class IbiteramoSerializer(serializers.ModelSerializer):
    class Meta:
         model = Ibiteramo
         fields = "__all__"

class ItikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itike
        fields = "__all__"        
