
from rest_framework import serializers
from .models import Computer, Site


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'hostname', 'bfid', 'site', 'created', 'updated', 'deleted')


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id','location','created', 'updated', 'deleted', 'operator',)