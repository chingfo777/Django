from rest_framework import serializers
from api.models import User
# create serializers here
# class CompanySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=Company
#         fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model=User
        fields="__all__"