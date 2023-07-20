from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

#Dont need
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

#Dont need
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ["name", "detail"]