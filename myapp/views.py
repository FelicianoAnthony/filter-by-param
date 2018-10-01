from django.shortcuts import render
from .models import Computer, Site
from rest_framework import viewsets
from .serializers import ComputerSerializer, SiteSerializer
from rest_framework import filters

from rest_framework.response import Response




class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

# class SearchComputers(viewsets.ModelViewSet):
# 	filter_backends = (filters.SearchFilter,) #allows for search functionality
# 	queryset = Computer.objects.filter(bfid=)


class ComputerViewSet(viewsets.ModelViewSet):
    #import pdb; pdb.set_trace()
    # queryset = Computer.objects.all()
    serializer_class = ComputerSerializer

    def get_queryset (self, *args, **kwargs):

        bfid = self.kwargs['comp']
        queryset = Computer.objects.filter(bfid=bfid)
        # import pdb; pdb.set_trace()
        return queryset


    # serializer_class = ComputerSerializer

