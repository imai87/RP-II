from django.shortcuts import render
from rest_framework_mongoengine import viewsets, generics

from .models import Atual, Ativos, Historico
from .serializers import AtualSerializer, AtivosSerializer, HistoricoSerializer


class AtualViewSet(viewsets.ModelViewSet):

    serializer_class = AtualSerializer

    def get_queryset(self):
        return Atual.objects.all()

class AtivosViewSet(viewsets.ModelViewSet):

    serializer_class = AtivosSerializer

    def get_queryset(self):
        return Ativos.objects.all()


#class HistoricoViewSet(viewsets.ModelViewSet, generics.ListAPIView):
#
#   serializer_class = HistoricoSerializer
#
#   def get_queryset(self):
#        stock = self.kwargs['stock']
#        return Historico.objects.filter(stock=stock)